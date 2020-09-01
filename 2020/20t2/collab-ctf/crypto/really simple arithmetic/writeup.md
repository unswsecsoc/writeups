### Writeup for Really Simple Arithmetic

## Author
* nhat286

## Category
* Crypto

## Description
Oh no help!!! I am trapped in the server of an evil org. that is stealing people's assignments and homework!
I managed to locate where they store their secret passphrase to unlock and free all stolen work,
but I can't seem to crack their code (I am terrible at Maths). Help solve the secret and we can go back to our normal life

## Ideas: Intro to RSA Crypto

## Solution
<details>

* Guess from the title (and some variable names in the challenge) that this is RSA, and understand the algorithm a bit (https://en.wikipedia.org/wiki/RSA_(cryptosystem))  
* 4 stages, each stage introduce concepts in the algorithm except the last one where you have to decrypt the message given the public key and encrypted message

    * Stage 1: Introducing public key N which is a multiple of 2 prime numbers. Given 1 prime number P and the public key N, find the other prime number by using division Q = N / P.
    * Stage 2: Introducing private key D which is the modular multiplicative inverse of publick key E modulo λ(n) (which is lcm(P-1, Q-1)).
        * Given public key N, we find 2 prime numbers P and Q which product is N = P * Q
        * Find λ(n) = lcm(P-1, Q-1)
        * Find D where D ≡ E^−1 (mod λ(n)) <=> D * E ≡ 1 (mod λ(n)) (google online for scripts or tools to find modular multiplicative inverse, or just simple use Maths and bruteforce D like in the solution script)
    * Stage 3: Introducing how to decrypt ciphertext. Given P, Q, E and the ciphertext, decrypt with private key D
        * Follow steps from stage 2 to find private key D
        * Decrypt the ciphertext with ((ciphertext ^ D) % N)
    * Stage 4: RSA. Apply everything you've learned so far to decrypt the ciphertext.
        * Find 2 prime factors of N (Navigation)
        * Figure out common exponent is 65537
        * Find private key D from P, Q and E
        * Decrypt the message with D and N
</details>