import socket

ip = '10.10.217.236'

ports = []

for i in range (1,10000):
	try:
		s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip,i))
		print("{} is open".format(i))
		port.append(i)
	except:
		pass


print(ports)
