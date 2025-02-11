import socket
import time

buffer_size = 65370
counter = 1

HOST = '0:0:0:0:0:0:0:1'
PORT = 7777

print("Connecting to Harvest Server...")

while buffer_size <= 65380:  # Adjusted loop condition
    server = (HOST, PORT)
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.connect(server)
    print("Connected!")

    buffer = b"A" * buffer_size  # Create buffer inside the loop
    print("Fuzzing Harvest with %s bytes" % len(buffer))
    s.send(buffer)
    s.close()

    buffer_size += counter
    time.sleep(5) # Adjusted sleep time
