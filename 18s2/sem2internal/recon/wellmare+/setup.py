#!/usr/bin/python

# setup.py
# consists of two main parts
# one part fo pull fake data from stackOverflow
# one part to post to GitHub Gist API, and hide the flag

# use -d <id> to delete a gist
# otherwise it will run and generate the gist with name 'scratchpad.txt'

import os, re, sys, requests, json
from bs4 import BeautifulSoup 

# check if Gist user credentials are set
# otherwise set the credentials (maybe use a fake account) 
iterations = 1
if len(sys.argv) < 2: iterations = 1
elif sys.argv[1] == "-d": pass
else: iterations = int(sys.argv[1])-1

if os.environ.get('GIST_USER') is None or \
   os.environ.get('GIST_PW') is None:	
	print("Set the proper credentials before running this script!")
	sys.exit(1)
else:
	user = str(os.environ.get('GIST_USER'))
	pw = str(os.environ.get('GIST_PW'))
	print("Using the following credentials:")
	print("Username: " + user) 
	print("Password: " + pw) 

# base url for github gists api
base = 'https://api.github.com/gists/'
links = []
posts = 'https://api.stackexchange.com/2.2/posts?order=desc&sort=activity&site=stackoverflow'
plant = '''
	/*----------------------------------------------------------------------------
	psssh noone will see these creds to my s3 bucket, just gonna delete it later

	AWS Access Key ID: AKIAJTKINJTX24ND7EDQ
	AWS Secret Access Key: 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
	-----------------------------------------------------------------------------*/
	'''

def delete(id):
	print("Deleting Gist ID: " + id) 
	r = requests.api.delete(base + id, auth=(user,pw))

	if(r.status_code == 204): print("[Success]")
	else: print("[Failed] - " + str(r.status_code))
	sys.exit(0)

# fills the "links" queue with URLs from stack overflow's API
def refill():
	global links
	r = requests.get(posts)		
	matches = re.findall("\"link\":\"([^\"]+)\"", r.text)
	links += matches 

# pull fake/ filler code from StackOverflow and plant in gist
def plantDecoy():
	global links
	if(links == []): refill()
	url = links.pop()
	r = requests.get(url)
	
	soup = BeautifulSoup(r.text, 'lxml')
	code = soup("code")
	if len(code) == 0: res = "<REDACTED>"
	else: res = max(code, key=len).text

	return res.replace('&lt;','<').replace('&gt;','>')

# check if we are deleting (mostly during debug phase)
if(len(sys.argv) == 3 and sys.argv[1] == '-d' and sys.argv[2] is not None):
	id = str(sys.argv[2])
	delete(id)

# Create a new gist
print("Creating new gist ...")
content = {"content": gist}
files = {"scratchpad.txt": content}
payload = {"public":False, "files":files}	 #### CHANGE TO FALSE FOR CHALLENGE #### 

r = requests.post(base[:-1], auth=(user,pw), data=json.dumps(payload))
if(r.status_code != 201): print ("[Failed] - " + str(r.status_code))

match = re.search("id\":\"([a-zA-Z0-9]{32})\"",r.text)
id = match.group(1)
print("New gist created = " + id)

# Main loop to insert fake data
print("Generating revisions")

for x in range(iterations): #real number would be 1337
	print("Revision:" + str(x+1))
	if(x == iterations/2): gist = plant
	else: gist = plantDecoy()
	payload = {"files": {"scratchpad.txt":{"content": gist}}}
	r = requests.api.patch(base + id, auth=(user,pw), data=json.dumps(payload))
	if(r.status_code != 200): print("[Edit failed] - " + str(r.status_code))

ans = raw_input("Delete the gist ["+str(id)+"] ? (y/n)")
if(ans == "y"): delete(id)
