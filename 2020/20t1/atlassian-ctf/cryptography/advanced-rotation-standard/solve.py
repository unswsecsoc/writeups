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

            self._iv = enced

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

if __name__ == '__main__':
    import base64 as b64
    import sys

    challenge = open(sys.argv[1]).read().strip().split('\n')
    ciphertext = b64.b64decode(challenge[0].split(' =')[1].strip())
    iv         = b64.b64decode(challenge[1].split(' =')[1].strip())
    key        = b64.b64decode(challenge[2].split(' =')[1].strip())

    a = ARS(iv, key)
    print(a.decrypt(ciphertext).decode())
