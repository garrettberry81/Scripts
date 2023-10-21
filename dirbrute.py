import requests

url ="http://10.10.217.236"

f = open('/root/wordlist2.txt', 'r')

wordlist = list(f.read().split ('\n'))

for i in wordlist:
	new_url = url + '/{}.html'.format(i)
	#print (new_url)
	r= requests.get(new_url)
	if r.status_code!=404:
		print(new_url)


f.close()
