import socket

ip = '10.10.217.236'

octets = list(ip.split('.'))

#print(octets)

for i in range (1,256):
	fullip= octets[0]+'.'+octets[1]+'.'+octets[2]+'.'+str(i)
	print (fullip)

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((fullip,7))
		print ("its valid")

	except:
		pass
