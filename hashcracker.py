
import hashlib

hash = '5030c5bd002de8713fef5daebd597620f5e8bcea31c603dccdfcdf502a57cc60'

f = open('/root/wordlist2.txt', 'r')

wordlist = list(f.read().split('\n'))

for i in wordlist:
	temphash = hashlib.sha256(i.encode())
	hexhash = temphash.hexdigest()
	if hexhash == hash:
		print (i)
		break

f.close()
