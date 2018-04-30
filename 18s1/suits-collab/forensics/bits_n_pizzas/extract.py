import random
import os

def main():
    directory = "shop"
    create(directory)
    print(join_files(directory))

def create(directory):
    with open("filenames.txt") as fi:
        filenames = set(fi.read().splitlines())

    files = split_file("flag")
    while len(files) != len(filenames):
        files = split_file("flag")

    try:
        os.makedirs(directory)
    except OSError:
        pass

    for strings in files:
        with open(os.path.join(directory, filenames.pop()), "wb") as fo:
           fo.write(strings)

def split_file(filename):

    files = []

    with open(filename, "rb") as fi:
        flag = bytearray(fi.read())

    while any(flag):
        randbits = rand_min_subset(flag)

        files.append(randbits)

        flag = bytearray(
            b - r
            for b, r in zip(flag, randbits)
        )
        
    return files

def join_files(directory):

    with open(os.path.join(directory, os.listdir(directory)[0]), "rb") as fi:
        peice_len = len(bytearray(fi.read()))
    original = bytearray(peice_len)

    for f in os.listdir(directory):
        with open(os.path.join(directory, f), "rb") as fi:
            peice = bytearray(fi.read())

        #print("".join(bin(i)[2:].rjust(8) for i in peice))

        original = bytearray(
            o + p
            for o, p in zip(original, peice)
        )
        #print("".join(bin(i)[2:].rjust(8) for i in original))

    return original

def rand_subset(array):
    return bytearray(
        random.randrange(byte + 1) & byte
        for byte in array
    )

def rand_min_subset(array):
    randbits = rand_subset(array)
    while not any(randbits):
        randbits = rand_subset(array)
    return randbits

if __name__ == "__main__":
    main()
