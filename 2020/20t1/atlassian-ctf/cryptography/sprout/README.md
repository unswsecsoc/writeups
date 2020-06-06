# Sprout

## Authors

* todo

## Category

* crypto

## Tags

_crypto_

## Description

Sprout is the latest anonymous message sharing board. We never store your keys and utilize the latest in
military grade AES encryption. Just try cracking our messages.

## Difficulty

* easy

## Points

75

## Hints

_None_

## Files

* src/snippets.py

## Setup

* Run the provided docker file

## Solution

_Code can be found in `solve.py`_

### Summary

This challenge involves exploiting a weak random seed.

#### Discovery

By viewing the page source, we see that the messages table originally contains a unix timestamp.

#### Exploiting

We seed a the python random algorithm with the discovered unix timestamp and generate keys and ivs for each message. We can then recover the plain text by running normal decryption.

### Flag

`ATLASSIAN{rN9_i5_n0T_R4nd0m}`