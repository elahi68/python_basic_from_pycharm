import socket

c = socket.socket()

c.connect(('192.168.120.151',9999))
#c.connect(('localhost',9999))
name = input('Enter your name: ')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())