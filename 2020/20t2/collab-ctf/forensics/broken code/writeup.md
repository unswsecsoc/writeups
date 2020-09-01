### Writeup for Really Simple Arithmetic

## Author
* nhat286

## Category
* Forensics

## Description
Someone sent me a promo code ... but my internet is sooooo laggy ... i think i lost a few bytes at the start ...
Can you help me get the code? I really like to use this for my brand new T-Shirt order!

## Ideas: Magic header bytes

## Solution
<details>

* Check the file extension -> PNG file
* Run command (in Linux) `file c0d3.png` -> can't detect file type, get `data` => maybe wrong format, or header bytes corrupted
* Check magic header bytes (usually the first 4 or 8 bytes) with `xxd c0d3.png | head` -> first 4 bytes are null bytes
* Look up header bytes for PNG file [(file header)](https://en.wikipedia.org/wiki/Portable_Network_Graphics) => fix up the first 4 bytes with `\x89\x50\x4e\x47`

</details>