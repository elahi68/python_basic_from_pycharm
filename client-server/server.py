import socket

s = socket.socket() #taking default IPV4 and TCP
print('Socket is created')

s.bind(('192.168.43.58',9999)) #bindidng ip with port number
#s.bind(('localhost',9999))
s.listen(3) #How many clients you wants to listen
print("Waiting for connection")

while True:
	c,addr = s.accept()
	c.send(bytes('accepted','utf-8'))
	name = c.recv(1024).decode()
	print('connected with client ',addr,name)

	c.send(bytes('Welcome...','utf-8'))

	c.close()