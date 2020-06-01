# Rot 256

## Authors

* todo

## Category

* crypto

## Tags

_crypto_

## Description

Everyone's favorite encryption scheme just got an upgrade.

## Difficulty

* easy

## Points

25

## Hints

_None_

## Files

* src/ciphertext
* src/rot256.py

## Setup

* Provide the given files

## Solution

_Code can be found in `solve.py`_

As there are only 256 possible keys you could just bruteforce all of them, alternatively as you know the flag starts with `ATLASSIAN{` you know the key must be the modular difference between the character code for `A` and the first byte of the ciphertext.

### Flag

`ATLASSIAN{rot_spu_tqv_urw_vsx_wty_xuz}`