import base64 as b64
import collections

class ARS:
    def __init__(self, iv, key):
        self._key = key
        self._iv  = iv
        self.BLOCK_SIZE = 16

    def encrypt(self, plaintext):
        out = []
        for block in self._blocks(plaintext):
            # 1. Rotate in the IV
            shuf = self.shuffle(block, self._iv)

            # 2. OTP the block cipher
            enced = self.rotate(shuf, self._key)

            out.append(enced)

            self._iv = shuf

        return b''.join(out)

    def decrypt(self, ciphertext):
        out = []
        for block in self._blocks(ciphertext):
            # 1. Perform the OTP decryption
            dec = self.unrotate(block, self._key)

            # 2. Rotate the IV
            roted = self.unshuffle(dec, self._iv)

            out.append(roted)

            self._iv = dec

        return b''.join(out)

    def rotate(self, text, key):
        return bytes([(text[i] + key[i]) % 256 for i in range(len(text))])

    def unrotate(self, text, key):
        return bytes([(text[i] - key[i]) % 256 for i in range(len(text))])

    def shuffle(self, text, key):
        # 1. Transform the text into a 4x4 matrix
        mtrx = [list(t) for t in (text[0:4], text[4:8], text[8:12], text[12:16])]

        # 2. Use the first half of the key to rotate the block vertically
        for k in range(0, 8, 2):
            col = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                first = mtrx[0][col]
                for i in range(3):
                    mtrx[i][col] = mtrx[i+1][col]
                mtrx[3][col] = first

        # 3. Use the second half of the key to rotate the block horizontally
        for k in range(8, 16, 2):
            row = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                first = mtrx[row][0]
                for i in range(3):
                    mtrx[row][i] = mtrx[row][i+1]
                mtrx[row][3] = first


        return b''.join(bytes(m) for m in mtrx)

    def unshuffle(self, text, key):
        # 1. Transform the text into a 4x4 matrix
        mtrx = [list(t) for t in (text[0:4], text[4:8], text[8:12], text[12:16])]

        # 2. Use the second half of the key to rotate the block horizontally
        for k in range(8, 16, 2):
            row = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                last = mtrx[row][-1]
                for i in range(2, -1, -1):
                    mtrx[row][i+1] = mtrx[row][i]
                mtrx[row][0] = last

        # 3. Use the first half of the key to rotate the block vertically
        for k in range(0, 8, 2):
            col = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                last = mtrx[-1][col]
                for i in range(2, -1, -1):
                    mtrx[i+1][col] = mtrx[i][col]
                mtrx[0][col] = last

        return b''.join(bytes(m) for m in mtrx)

    def _blocks(self, plaintext):
        for i in range(0, len(plaintext), 16):
            yield plaintext[i:i+16]

memo = {}
def pairs(n):
    if n in memo:
        return memo[n]

    arr = []
    for i in range(n+1):
        arr.append((i, n-i))
    memo[n] = arr
    return arr

def quads(n):
    root_pairs = pairs(n)
    for pair in root_pairs:
        lp = pairs(pair[0])
        rp = pairs(pair[1])

        for l in lp:
            for r in rp:
                yield l + r

def bf_rotations():
    s = set()
    for t in range(12+1):
        for q in quads(t):
            s.add(tuple([i % 4 for i in q]))

    for it in s:
        yield bytes([0, it[0], 1, it[1], 2, it[2], 3, it[3]])

def starts_with(bstr, s):
    return all(bstr[i] == ord(s[i]) for i in range(len(s)))

def leet_decode(s):
    encoded   = list(b'4bcd3f6h1jklmn0pqr57uvwxyz')
    decodable = [ord(x) for x in string.ascii_lowercase]
    mapping = {encoded[i]: decodable[i] for i in range(len(encoded))}
    return bytes([mapping[c] if c in mapping else c for c in s.lower()])

def ioc(s):
    f = collections.Counter(s)
    num = sum(v * (v-1) for v in f.values())
    den = len(s) * (len(s)-1)/27
    return num/den

def word_count(string, corpus, delim='_'):
    words = string.split(delim)
    return sum(1 for word in words if word in corpus)

if __name__ == '__main__':
    import sys
    import string
    import itertools

    # Charset we assume the flag has
    CHARSET = (string.ascii_letters + string.digits + '}{_').encode()
    # Byte we assume isnt in the key, this can realisticly be anything, and such a value must exist
    PLACEHOLDER = b'\x00'

    util = ARS('', '')
    ciphertext = b64.b64decode(open(sys.argv[1]).read())

    blocks = list(util._blocks(ciphertext))
    rotations = list(bf_rotations())
    poss_ivs = [r1 + r2 for r1 in rotations for r2 in rotations]
    bflag = 'ATLASSIAN{'.encode()
    bflag += PLACEHOLDER * (16 - len(bflag))

    poss_keys = []
    poss_key_offsets = [[set() for _ in range(len(blocks))] for __ in range(len(blocks[0]))]
    for ci in range(len(blocks[0])):
        for ri, r in enumerate(blocks):
            for i in range(256):
                if (r[ci] - i) % 256 in CHARSET:
                    poss_key_offsets[ci][ri].add(i)
    for i in range(len(poss_key_offsets)):
        x = poss_key_offsets[i][0]
        for it in poss_key_offsets[i][1:]:
            x = x.intersection(it)
        poss_keys.append(x)

    # Create possible plaintext arrangements for every possible iv
    plaintexts = set()
    for piv in poss_ivs:
        plaintexts.add((util.shuffle(bflag, piv), piv))

    # Reduce the number of ivs by enforcing that any iv/plaintext pair must also
    # decrypt other blocks to characters that are in the charset
    posstexts = set()
    for pt, iv in plaintexts:
        # Guess a key (C = P + K <==> K = C - P)
        key = util.unrotate(blocks[0], pt)
        possible = True

        # For every block, a decryption with the guessed key should result in
        #  valid character (i.e. in CHARSET) for applicable positions
        # Note we don't care about order here as all characters in the block are assumed to be bytes
        #  (theres no padding functionality in the original encryption program)
        for block in blocks:
            block_guess = util.unrotate(block, key)
            for i in range(16):
                if pt[i] == ord(PLACEHOLDER): continue

                if block_guess[i] not in CHARSET:
                    possible = False
                    break
            if not possible:
                break

        if possible:
            posstexts.add((pt, key, iv))

    print(f'Reduced down to {len(posstexts)} possible ivs')

    # Once we have that bruteforce all possible keys
    #  We search for placeholder in the plaintext to detect bytes in the key which are non-meaningful
    #  We replace these with a guess and decode all possible guesses
    possflags = set()
    for pt, key, iv in posstexts:
        zeros = []
        for i in range(16):
            if pt[i] == 0:
                key[i] == PLACEHOLDER
                zeros.append(i)

        p = 1
        for z in zeros:
            p *= len(poss_keys[z])
        print(f'  Enumerating {p} keys')

        # Bruteforce the key
        #  We look for resultant candidates that have exactly one {, exactly one }, ends in }, and does not have __ (which would indicate a zero length word)
        ki = list(key)
        for blanks in itertools.product(*[poss_keys[z] for z in zeros]):
            for i, k in enumerate(blanks):
                ki[zeros[i]] = k

            h = ARS(iv, bytes(ki))
            dec = h.decrypt(ciphertext)
            if dec[-1] == ord('}') and dec.count(b'}') == 1 and dec.count('{'.encode()) == 1 and b'__' not in dec:
                possflags.add(dec)

    print(f'Found {len(possflags)} possible flags')

    # Once we have a smaller array of possible flags we determine how english like they are
    #  We first leet decode them, and then on the resultant array we run a ioc check as well as ensure
    #   there are no digits in the decoded text
    dig = set([c for c in string.digits.encode()])
    decoded_flags = set()
    for possflag in possflags:
        flag = leet_decode(possflag)
        content = flag.split('{'.encode())[1][:-1]
        if all(c not in dig for c in content) and abs(1.73 - ioc(content)) < 0.1:
            decoded_flags.add((possflag, flag))

    print(f'Found {len(decoded_flags)} decoded flags')

    # Finally we rank all the english like string based on how many words we can find in them
    corpus = set(open('/usr/share/dict/google/10000-english.txt').read().strip().split('\n'))
    ranked_flags = list(sorted(decoded_flags, key=lambda guess: word_count(guess[1].decode().split('{')[1][:-1], corpus), reverse=True))
    for i, (flag, _) in enumerate(ranked_flags[:10]):
        print(f'Guess #{i}: {flag.decode()}')