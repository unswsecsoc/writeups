# Assignment 1

## Author
Vicknesh

## Category
Reversing

## Description
Hey professor, I forgot the password to my assignment and the dog ate my source code. I've attached what I have. Could I please get an extension ... jk ... unless?

## Difficulty
easy

## Points
50

## Files
assign1: an executable which when launched asks for a password which the competitor doesn't know

## Solution
<details>
<summary>spoiler</summary>

### Idea
To make a simple reverse engineering problem

### Walkthrough
1. Open the file using a text editor such as vim and you can quickly find out that it was compiled from python 3.8 code
2. A google search will show that this can be done using pyinstaller.
3. You can use a pyinstaller extractor such as this one: https://github.com/extremecoders-re/pyinstxtractor, to extract the .pyc files from the executable
4. One of the .pyc files will be called assign1.pyc. Being that this is the same name as the executable, this should be the file that contains the source code. Then, use uncompyle to return the .pyc to its original source code and you can find the flag

### Flag
`ATLASSIAN{WHA15_tH3_P01nt_0f_ha5H1ng_aAC6Bstvo}`
</details>
