import random
import string


def constant_strncmp(a: str, b: str, length: int) -> bool:
    """Constant time strncmp function

We do not use Python's built in comparison function because it is
vulnerable to timing attacks.

This function will perform a comparison regardless of the length or match of the input strings.

This way, time taken to compare two strings is constant and it will prevent timing attacks.
"""

    dummy1 = random.choice(string.ascii_letters)
    dummy2 = random.choice(string.ascii_letters)
    volatile = False

    for i in range(0, length):
        # If index out of bounds
        if i + 1 > len(a) or i + 1 > len(b):
            if dummy1 == dummy2:
                volatile = not volatile

        if a[i] != b[i]:
            return False

    return True


print(constant_strncmp("hello", "hello world", len("hello world")))

"""
I'm trying to write a constant time string compare function to stop timing attacks

Does anyone know what I'm doing wrong here? Thanks

/usr/bin/python /home/jonathan/Company-Projects/mips64me/test.py
Traceback (most recent call last):
  File "/home/jonathan/Company-Projects/mips64me/test.py", line 32, in <module>
    print(constant_strncmp("hello", "hello world", len("hello world")))
  File "/home/jonathan/Company-Projects/mips64me/test.py", line 26, in constant_strncmp
    if a[i] != b[i]:
IndexError: string index out of range
"""