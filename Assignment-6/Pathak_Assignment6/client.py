import socket
import sys

# file = sys.argv[1]
e = socket.socket()
print("Socket successfully created")

port = 6500

e.connect(('127.0.0.1',port))

fil = open("images.jpeg", "rb")
print(fil)
data = fil.read(2048)

while data:
    e.send(data)
    data = fil.read(2048)

msg = e.recv(1024)
print("How's Going?")
while msg:
    print('Received:' + msg.decode())
    msg = e.recv(1024)
print("Hey! Sagar Pathak here")
fil.close()

e.close()
