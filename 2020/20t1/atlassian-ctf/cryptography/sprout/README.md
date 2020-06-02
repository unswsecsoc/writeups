# Sprout

## Authors
* todo

## Category
* Crypto

## Tags
* Seed Exploit

## Description
Sprout is the latest anonymous message sharing board. We never store your keys and utilize the latest in
military grade AES encryption. Just try cracking our messages.

## Difficulty
* easy

## Points
100

## Hints
N/A

## Files
* src/src/snippets.py

## Setup
1. Run the provided docker file

## Solution
<details>
<summary>spoiler</summary>

### Description
This challenge involves exploiting a weak random seed.

#### Discovery
By curling the page (or disabling javascript), we see that the messages table originally contains a unix timestamp.

#### Exploiting
We seed a the python random algorithm with the disocvered unix timestamp and generate keys and ivs for each message. We can then recover the plain text by running normal decryption.

### Flag
`ATLASSIAN{rN9_i5_n0T_R4nd0m}`

</details>
