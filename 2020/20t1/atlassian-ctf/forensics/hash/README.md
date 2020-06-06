# H@sh

## Authors
* p1gc0rn

## Category
* Forensics

## Tags
* MacOSX

## Description
What is the hash of the file?
Note: The next challenge needs using the file again is Goldfish and P@ssw0rd.

## Difficulty
* very easy

## Points
50

## Hints
1. N/A

## Files
* mem.raw [800mb download here](https://drive.google.com/file/d/1-t9-2uXzVjPghOVYP_K2jYyMOYj0r82Z/view?usp=sharing)

## Solution
<details>
<summary>spoiler</summary>

### Idea
Check the integrity of the file by checking the md5 hash of the file

### Walkthrough
The command `md5sum mem.raw` will produce the hash
### Flag
The finding is the hash which needs wrapping with flag format.
`ATLASSIAN{b26ab2e30513bba9780fd40910ef3c92}`
</details>
