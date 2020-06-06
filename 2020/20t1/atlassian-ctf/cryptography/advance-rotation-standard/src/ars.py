class ARS:
    def __init__(self, iv, key):
        self._key = key
        self._iv  = iv
        self.BLOCK_SIZE = 16

    def encrypt(self, plaintext):
        out = []
        for block in self._blocks(plaintext):
            shuf = self.shuffle(block, self._iv)
            enced = self.rotate(shuf, self._key)

            out.append(enced)

            self._iv = shuf

        return b''.join(out)

    def rotate(self, text, key):
        return bytes([(text[i] + key[i]) % 256 for i in range(len(text))])

    def shuffle(self, text, key):
        mtrx = [list(t) for t in (text[0:4], text[4:8], text[8:12], text[12:16])]

        for k in range(0, 8, 2):
            col = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                first = mtrx[0][col]
                for i in range(3):
                    mtrx[i][col] = mtrx[i+1][col]
                mtrx[3][col] = first

        for k in range(8, 16, 2):
            row = key[k]   % 4
            rot = key[k+1] % 4

            for _ in range(rot):
                first = mtrx[row][0]
                for i in range(3):
                    mtrx[row][i] = mtrx[row][i+1]
                mtrx[row][3] = first


        return b''.join(bytes(m) for m in mtrx)

    def _blocks(self, plaintext):
        for i in range(0, len(plaintext), 16):
            yield plaintext[i:i+16]

if __name__ == '__main__':
    import sys
    import secrets
    import base64 as b64

    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <plaintext> [iv] [key]', file=sys.stderr)
        sys.exit(1)

    key = secrets.token_bytes(16) if len(sys.argv) < 4 else sys.argv[3].encode()
    iv  = secrets.token_bytes(16) if len(sys.argv) < 4 else sys.argv[2].encode()

    handle = ARS(iv, key)
    print(f'cipher = {b64.b64encode(handle.encrypt(sys.argv[1].encode())).decode()}')
    print(f'iv     = {b64.b64encode(iv).decode()}')
    print(f'key    = {b64.b64encode(key).decode()}')
