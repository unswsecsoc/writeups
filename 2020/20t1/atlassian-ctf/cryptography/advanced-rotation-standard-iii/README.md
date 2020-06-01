# Advanced Rotation Standard III

## Authors

* todo

## Category

* crypto

## Tags

_crypto_, _advanced rotation standard_

## Description

You had help for the last 2 challenges. Not for this one... Crack the ciphertext.

**Flag Format:**
The flag is similar to previous flags. It consits of a series of partially l33tsp34k encoded
english words (or acronyms) separated by '_'.

I.e. flag = `ATLASSIAN\{[A-Za-z0-9]+(_[A-Za-z0-9]+)+\}`

It is recommended to use a fast programming language / intepreter. For example, pypy will drastically speed up your solution for python.
A non-optimal solution takes on 1 core (Intel i7-6700HQ @ 3.500GHz):
```text
30s    - PyPy3
3m 15s - Python3 (CPython)
```

## Difficulty

* hard

## Points

200

## Hints

1. Partially l33tsp34k encoded english words (or acronyms) - `decrypt_char(ciphertext[i], key[i]) ∈ CHARSET`

## Files

* src/ars.py
* src/challenge.txt

## Setup

* None. Provide the given files

## Solution

_Code can be found in `solve.py`_

### Preamble

This is a very challenging problem, it is important to keep in mind throughout that we are interested in cracking the provided ciphertext specifically. We don't care about a general solve. It is also to keep in mind the restrictions on the flag. They're defined for a reason.

### Summary

We approach this challenge in 4 steps.

1. First we aim select a very small subset of ivs
2. For each iv we aim to extract a series of "correct" keys
3. For each key and its associated iv we produce a decryption candidate and we evaluate to see if its a possible flag
4. We select the correct flag from the possible flags

### IV Selection

We first want to reduce the 65536 possible ivs down to a more manageable subset. In order to do this we first bruteforce all ivs in order to to generate a series of plaintext permutations based on the knowledge that the first 10 characters of the plaintext must be `ATLASSIAN{`. Based on each plaintext permutation we can calculate a key candidate. We use this key candidate to `unrotate` each following block. We know that regardless of how the block is shuffled, such a unrotation needs to always result in a letter, number or '\_{}'. If this is true over all 4 blocks we mark the iv as possible. Otherwise we discard it.

Using this strategy we are able to reduce the search space down to just 6 IVs.

### Key Production

For each iv we then consider all possible keys. As we know the plaintext starts with `ATLASSIAN{` we already know 10 characters of the key, and only need to bruteforce 6 more. However just considering `256^6 > 200 trillion` keys is not feasible. We add the additional constraint that `n`th byte of a key must be able produce a character in our charset when subtracted from the `n`th character across all blocks. This constraint by itself is enough to reduce the search space for keys to less than 1 million per iv.

### Key Selection

For each produced key for a given iv, we then attempt to decrypt the message. We filter out all messages which have more than 1 of '{' or '}', or messages where there are zero length words ('\_\_'). We also require the last character to be a '}'. We accumulate all such key/plaintexts over all ivs.

This reduces the total search space to less than 300000 flags.

## Flag selection

For every possible key, we then perform a l33t decoding of the contents. This will result in a (mostly) english string. We can determine how "english-like" a string using 2 strategies.

1. Calculate its incidence of coincidence and compare it to english, discarding flags which are too dissimilar
2. Search for non-letter (or underscore) characters and discarding flags which match

Now we have a very small set of possible english-like flags. At this point a human may be able to read over all flags. However in order to expediate the process, we rank each potential flag by the number of english words we can find in it (by searching against a list of common words). _Note you don't actually have to do this_

The flag with the most english words is our final flag.

### Flag
`ATLASSIAN{ARS_r34Lly_m3aN5_Arb17R4r1Ly_R34D4BL3_57r1n6_EnC0d1n6}`