import sys
with open("c0d3.png", "rb") as inf:
    s = inf.read()

head = "\x89PNG"
with open("./flag.png", "wb") as out:
    out.write(head + s[len(head):])
