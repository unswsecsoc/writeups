from string import ascii_lowercase
ORDER = len(ascii_lowercase)

def main():
    #flag = "flag{iamthomasthetankengine}"
    flag = "flag{choochooomotherfuckers}"
    print(roll(flag), roll(roll(flag), decode=True))

def rot(string, num):
    encoding = str.maketrans(
        ascii_lowercase,
        ascii_lowercase[num % ORDER:] + ascii_lowercase[:num % ORDER]
    )
    return string.translate(encoding)

def roll(string, decode=False):
    offset = start = -1 # 0
    for i in range(1, len(string)):
        if not string[i + start].isalpha():
            offset += 1
        string = (
            string[:i + offset]
            + rot(
                string[i + offset:],
                i if not decode else ORDER - i,
            )
        )
    return string

if __name__ == "__main__":
    main()
