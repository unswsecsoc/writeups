import base64

def main():
    string = b"flag{_b45e_z3r0_p01nt_51x_f0ur_}"
    encoded = encode(string, 5)
    print(encoded)
    decoded = decode(encoded, 5)
    print(decoded)

def half(string):
    mid = len(string) // 2
    left, right = string[:mid], string[mid:]
    return left, right

def encode(string, count):
    if count:
        left, right = map(base64.b64encode, half(string))
        return encode(left, count - 1) + encode(right, count - 1)
    else:
        return string

def decode(string, count):
    if count:
        left, right = half(string)
        return (
            base64.b64decode(
                decode(left, count - 1)
            )
            + base64.b64decode(
                decode(right, count - 1)
            )
        )
    else:
        return string

if __name__ == "__main__":
    main()

