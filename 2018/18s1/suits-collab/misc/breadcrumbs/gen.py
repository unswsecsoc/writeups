import random
import itertools
import string
import base64
import os

DIRECTORY = "breadcrumbs"
FLAG = "FLAG{h4n53l_&_gr3t3l}"

def make_secret(data, filename):
    '''
    b64 = base64.b64encode(data.encode())
    with open(filename, 'wb') as fo:
        fo.write(b64)
    '''
    with open(filename, 'w') as fo:
        fo.write(data)

def decode_file(filename):
    '''
    with open(filename, 'rb') as fi:
        b64 = fi.read()
    return base64.b64decode(b64).decode()
    '''
    with open(filename) as fi:
        return fi.read()

def generate_secrets(flag_string, directory, symbols, length):

    try:
        os.makedirs(DIRECTORY)
    except OSError as e:
        os.chmod(DIRECTORY, 0o755) 
        for filename in os.listdir(directory):
            os.remove(os.path.join(directory, filename))

    print("generating codes...")
    codes = [ 
        "".join(item)
        for item in 
        itertools.product(symbols, repeat = length)
    ]

    print("shuuffling codes...")
    random.shuffle(codes)
    *codes, last_code, flag_code = codes 

    for from_code, to_code in zip(
        ("start", *codes),
        (*codes, last_code)
    ):
        to_file = to_code
        from_file = os.path.join(directory, from_code)
        #print("creating", from_file)
        make_secret(to_file, from_file)
        os.chmod(from_file, 0o744)

    print("last herring is:", last_code)
    print("flag is in", flag_code)
    make_secret(flag_string, os.path.join(directory, flag_code))
    print("done!")
    os.chmod(DIRECTORY, 711) 


def solve(directory, start):
    seen = set()

    data = decode_file(os.path.join(directory, start))
    seen.add(int(data))
    max_seen = 0
    while True:
        try:
            data = decode_file(os.path.join(directory, data))
            seen.add(int(data))
            max_seen = max(int(data), max_seen)
        except:
            print("stopped at:", data)
            break
    return (set(range(max_seen + 1)) - seen).pop()
    
if __name__ == "__main__":
    generate_secrets(FLAG, DIRECTORY, string.digits, 6)
    print("solving...")
    print("flag is at: ", solve(DIRECTORY, "start"))



    



            





    

    




