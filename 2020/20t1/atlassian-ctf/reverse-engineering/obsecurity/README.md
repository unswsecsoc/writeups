# Obsecurity

## Authors
* Matthew Turner (@DeadlyFugu)

## Category
* Reversing

## Description
Obsecurity, it's the latest fad in the cubersecurity world! If you write code for a virtual machine no-one has ever heard of before, the hackers won't have any tools to hack it!

## Difficulty
* medium

## Points
100

## Solution
<details>
<summary>spoiler</summary>

### Idea
A virtual machine, as well as a program for it, are provided. Upon running
the program, it will ask the user for a password. Analysing the program
allows one to extract the password, which can then be used to get the flag.

### Walkthrough
Walkthrough by: amamiya/nullpo of team ramzimustfinishalienisolation.

Looking at the files provided, we see an executable, its source code and
a mystery binary. Opening the source code, we're greeted with opcodes,
memory, and registers, which immediately leads me to think that it's
some sort of assembly emulator, and scrolling down, that's exactly what
it is. It even provides us with a descriptor of each opcode and its C
implementation. Running the program just asks for a password, which, if
it's incorrect, just tells us it's incorrect and quits. Since we already
have the source code and the program, we can quickly modify the program
to convert the mystery binary to human-readable assembly code
(attached). Of particular interest here are 26 CMP instructions between
43 and f7. Once again, since we already have the source code it's
trivial to edit and recompile it to print out exactly what's being
compared, and we input any 26 characters as the password and get the
following output:

```
CMP 30, 61
CMP 62, 61
CMP 73, 61
CMP 33, 61
CMP 63, 61
CMP 55, 61
CMP 52, 61
CMP 31, 61
CMP 74, 61
CMP 59, 61
CMP 2d, 61
CMP 31, 61
CMP 73, 61
CMP 2d, 61
CMP 4e, 61
CMP 30, 61
CMP 2d, 61
CMP 6d, 61
CMP 34, 61
CMP 54, 61
CMP 43, 61
CMP 68, 61
CMP 2d, 61
CMP 66, 61
CMP 30, 61
CMP 52, 61
```

It turns out the program directly compares our input to (presumably)
what is the plaintext password. Converting the first half of the CMPs to
ASCII from hex, we get "0bs3cUR1tY-1s-N0-m4TCh-f0R". Running the program
once more, we input that as the password and it outputs the flag.

### Flag
`ATLASSIAN{SOmE0n3-w1Th-t0o-MucH-t1M3}`
</details>
