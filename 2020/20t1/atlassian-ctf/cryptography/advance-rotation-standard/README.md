# Advanced Rotation Standard

## Authors
* todo

## Category
* Crypto

## Tags
N/A

## Description
You have the source code, message, key and IV, all thats left is the decryption function.

## Difficulty
* easy

## Points
50

## Hints
N/A

## Files
* src/ars.py
* src/challenge.txt

## Setup
* Docker build the given docker file

## Solution
<details>
<summary>spoiler</summary>

### Description
The goal of the challenge is pretty self explanatory. We need to write a decryption function based on the existing encryption function.

We note that there are two main operations per block during encryption.
1. The plaintext is shuffled using the `shuffle` method
2. The plaintext is added to the key using the `rotate` method

For our decryption function we would then like to run `[un]rotate` followed by `[un]shuffle`. We can then figure out how to chain blocks.

### Unrotate
First we write the `unrotate` function. The rotate function (below) simply adds the ascii values of the two corresponding characters in each block.
```python
def rotate(self, text, key):
    return bytes([(text[i] + key[i]) % 256 for i in range(len(text))])
```

As addition under mod is trivially reversable by subtraction, we replace the `+` with a `-` and get our unrotate function
```python
def unrotate(self, text, key):
    return bytes([(text[i] - key[i]) % 256 for i in range(len(text))])
```

#### Unshuffle
The shuffle function first transforms the text into a 4x4 matrix of characters. The first loop will the rotate each column, whilst the second loop rotates each row. The amount and row to rotate is specified by the iv.

For example, for a iv `3 2 000000 2 1 000000` on text `abcdefghijklmnop`:

We first transform to a 4x4 matrix
```
abcd
efgh
ijkl
mnop
```

We rotate up the `3`th column `2` times.
```
abcl
efgp
ijkd
mnoh
```

We rotate left the `2`th row `1` time.
```
abcl
efgp
jkdi
mnoh
```

We then flatten the matrix to get `abclefgpjkdimnoh`.

In order to reverse this, we then want to unrotate each row, followed by each column, in the reverse order they were shuffled in (code for this is in `solve.py`).

### Chaining
Finally the encryption function set the next iv based on the shuffled plaintext of the current block. We can replicate this by setting our next iv to be the unrotated (and hence shuffled) decrypted text of the current block.

### Flag
`ATLASSIAN{r0ll_your_pWn_enkryp+i0n_w4t_COuLd_p055iblY_GO_wrong?}`

</details>
