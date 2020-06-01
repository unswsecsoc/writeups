# Advanced Rotation Standard II

## Authors
* todo

## Category
* crypto

## Tags
_crypto_, _advanced rotation standard_

## Description

I made a app that encrypts messages with ARS for you! The government says I have to be
able to decrypt anything someone encrypts using my app, so I've used the same key for all the messages.
What could go wrong?

_Note: It's benificial to have done ARS1 first_

## Difficulty

* medium

## Points

100

## Hints

_None_

## Files

* src/ars.py
* src/app.py
* src/challenge.txt

## Setup

* Docker build the given docker file

## Solution

_Code can be found in `solve.py`_

### Description

Here we aim to decrypt the given ciphertext without knowledge of the IV and key. However we can send arbitrary plaintexts and get a ciphertext with the same key and IV as the provided ciphertext.

We can use this knowledge to perform a chosen plaintext attack in order to retrieve the key. We then two alternative methods to obtain the IV; one involving bruteforce, and another involving a second chosen plaintext.

_Note that solutions are described under the assumption that padding has been removed_

### Key retrieval

We notice that the key is used in the following rotate function. This adds the key's value and the plaintext's value mod 256. If we send a plaintext consisting soley of `\x00`s this would attempt to add 0 to every value of the key, and would thus just return the key.
```python
def rotate(self, text, key):
    return bytes([(text[i] + key[i]) % 256 for i in range(len(text))])
```

We hence have the `key`.

### IV Bruteforce

Once we have the key, the order is scrambled due to the shuffle operation. We need to unscramble the key in order to be able to decrypt the ciphertext. Simply trying every shuffle of the key is not feasible as that would require `16! > 20 trillion` operations.

Similarly we cannot bruteforce every 16 character iv, as this would take `256^16 > 10^38` operations. We do however notice that the way in which the iv encodes rotation information is flawed. For every pair of bytes in the iv e.g. `aabbccddeeff...` the first byte encodes the row/column to rotate, and the second byte encodes how many time the rotation should be performed. As there are only 4 rows/columns any value greater than 4 can be effectively modded by 4.

For example if the first two bytes of the iv were `200 130` this would say to rotate the 200th column 130 times. However as there is no 200th column, this simply takes the `200 % 4 = 0`th column, and as each column in the matrix only has 4 elements rotating 130 times is equivalent to rotating `130 % 4 = 2` times.

Hence for a IV simplified like this there are only `4^16 = 4 billion` possibilities.

However as most laptops would still take a few days to perform such a calculation we need to restrict the iv further. We notice that we can summarize rotations. For example `1 1 1 2` says to rotate column 1 once, and then rotate column 1 twice. This could simply just be stated as rotate column 1 thrice.

We can hence just fix all the columns `0 a 1 b 2 c 3 d ...` and bruteforce all the rotation amount (subject to `a+b+c+d < 12`). This yields `4^8 = 65536` possible effective ivs, which can be easily bruteforced by any computer.

### IV Leak

Alternatively as the IV is fixed for all requests, we can use a chosen plaintext to obtain the iv order. We begin by sending a ordered block of text `1234567890abcdef` and perform a decryption using the key we found earlier.
This will leave us with a scrambled version of the original text. `scramble(1234567890abcdef) = c2e43816507b9daf`. We know that the scambling function must have placed `1` in the 7th position, `2` in he 2nd position, `3` in the 5th, etc.
By reversing the scrambling we can obtain the first block of the key `ATLASSIAN{cho0se`.

### Finding the solution

We conduct either of the above solutions and select the possible flags.

### Flag

`ATLASSIAN{cho0se_4_flA9_4ny_F1AG_ooo_or_d0nt_it5_Up_2_u}`