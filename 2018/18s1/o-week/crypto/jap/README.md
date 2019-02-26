# コードトーク

## Author
* weilon

## Category
Cryptography

## Type
* cipher
* language

## Description
### Lost in Translation
Please see the attached message from Hiro for your challenge.

## Points
20

## Hints
1. I guess you could say that sometimes things are lost in translation...
2. The decoded passphrase is in English. Also, don't take this as one giant Japanese phrase. Look closer.
3. This challenge is essentially a really fancy substitution cipher. What could each word represent?

## Files
- コードトーク.txt: Contains ciphertext and instructions.

## Walkthrough
1. Translate each Japanese word (they're space separated) into their English equivalent
2. Take the first letter of each of those English words, and combine them together
3. Further explanation:
    - 氷 translates to "ice", 動物 = "animal" and お金 = money.
    - If we take the first letter of each translated English word, we get 'I', 'A', 'M'.
    - Repeating this processes gives us 'IAMFROMSAITAMA', which is the answer.

## Flag
`FLAG{IAMFROMSAITAMA}`

## Other
A similar technique was actually used by the United States during the Second World War. Native Americans were recruited as code talkers to transmit coded messages using their native language. See http://www.nmai.si.edu/education/codetalkers/html/chapter4.html

