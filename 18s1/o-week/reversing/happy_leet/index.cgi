#!/web/cs2041/bin/python3.6.3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
string = form.getvalue("input", "")
ascii_values = [ord(c) for c in string]
output = sum(ascii_values[::2]) - sum(ascii_values[1::2])

correct = output == 1337

flag = """
<h3>Thanks for the good time ^_^ here is your flag!</br>
FLAG{asc!!_what_you_d!d_there}<h3>
""" if correct else ""

face = ":)" if correct else ":("

print("Content-type: text/html\n")

print(f"""
<html>
    <head><title>Happy Little Leet</title></head>
    <body>
        <h1>Happy Little Leet</h1>
        <h2>Can you make me a happy little 1337?</h2>
        <h3>SHOW ME WHAT YOU GOT!</h3>
        <form method="post" id="form">
            <p><input type="text" name="input" value="{string}" autofocus/><button type="submit" form="form">{face}</button></p>
        </form>
        <p><strong>Result: </strong>{output if output else ""}</p>
        {flag}
        <h5><a href="http://www.unswsecurity.com/">UNSW Security Society</a> | <a href="https://ctf.unswsecurity.com/">O-Week CTF</a></h5>
    </body>
</html>
""")

