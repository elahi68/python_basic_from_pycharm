import socket

hostname = socket.gethostname()
print ('hostname: ',hostname)

local_ip = socket.gethostbyname(hostname)

print ("local ip address : ",local_ip)