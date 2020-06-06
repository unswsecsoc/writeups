import base64 as b64

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

def remote_encrypt(msg):
    """ Fill this in with some method of getting the b64 decoded encrypted string from app """
    assert msg == b"\x00" * 16
    return b64.b64decode('BlRiNbVo3K/40ntvzLCIqBZkckXFeOy/COKLf9zAmLg=')[:16]


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

if __name__ == '__main__':
    import sys

    chosen = b"\x00" * 16
    key = remote_encrypt(chosen)
    ciphertext = b64.b64decode(open(sys.argv[1], 'r').read())
    print(ciphertext)

    flags = []
    for hrot in bf_rotations():
        for vrot in bf_rotations():
            rot = hrot + vrot

            a = ARS(rot, key)
            dec = a.decrypt(ciphertext)
            if starts_with(dec, 'ATLASSIAN{'):
                flags.append(dec)

    # Realistically at this point you could extract the flag by eye
    print('\n'.join(f.decode() for f in flags))

    # If you wanted to you could check the remote_encryption matches
    """
    for flag in flags:
        if remote_encrypt(flag) == ciphertext:
            print(flag)
            break
    """
