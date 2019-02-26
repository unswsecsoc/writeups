#!/usr/bin/python3

code = input("Enter code: ").split(".")
current = 0
for characters in code:
    for char in characters:
        if char == '+':
            current += 1
        else:
            current -= 1
    print(chr(current), end="")
print()

