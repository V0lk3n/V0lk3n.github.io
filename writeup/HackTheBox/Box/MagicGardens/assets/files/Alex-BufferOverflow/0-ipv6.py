import socket
import time

HOST = '0:0:0:0:0:0:0:1'
PORT = 7777

packets = b"HelloThere"

print("Connecting to Harvest Server...")

server = (HOST, PORT)
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect(server)
print("Connected!")

print("Sending some testing packets")
s.send(packets)
s.close()

