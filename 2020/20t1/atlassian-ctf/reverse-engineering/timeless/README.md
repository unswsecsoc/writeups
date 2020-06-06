# Timeless

## Authors
* Matthew Turner (@DeadlyFugu)

## Category
* Reversing

## Description
Hear ye, hear ye! Hither I bringeth thee a cypher so stout thy writ
letters, sans thy key, shalt beest perused nevermore.

## Difficulty
* medium

## Points
100

## Solution
<details>
<summary>spoiler</summary>

### Idea
In this challenge you are given an encrypted file an a program to
encrypt/decrypt. By reverse engineering the binary, one will find that
it encrypts the file against a stream of random bytes. Although the RNG
is relatively secure, it is seeded by time(0) which can be predicted
based on the file's timestamp.

### Walkthrough
1. We can disassemble the binary using objdump. In reality, you should probably use a more practical reversing tool (IDA, Binja, Radare, etc.) instead to get a general picture of how it works.
```
$ objdump -M intel -d timeless | less
```
2. Of most interest to us are probably the functions `encrypt` and `decrypt`. Within `encrypt`, we can see that the RNG is seeded (call to `musl_srand`) using `time(0)`. The `process_chunk` function proceeds to XOR each byte of the file against a value from `secure_rand8` - which depends only on the state of the RNG, not the password. In fact, the password is really only used to encrypt the seed before storing it in the file at offset 8.
3. Note that `time(0)` returns the current time in seconds since the Unix epoch. This means that the seed used for the file can be guessed based on it's metadata - it's late modified date. Get the date in second-since-epoch form:
```
$ stat -c %Y shakespeare.txt.tl
1588924887
```
4. Referring back to the disassembly, in `decrypt`, we can see a call to `musl_srand` to seed the RNG again. Specifically, the call to musl_srand happens at address 0x4017a7 and the seed is stored in the edi register.
5. We can now run our executable under GDB and insert a breakpoint at the call to `musl_srand`. This will let us modify the seed as it runs.
```
$ gdb timeless
(gdb) break *0x4017a7
Breakpoint 1 at 0x4017a7
(gdb) run shakespeare.txt.tl
Starting program: /path/to/timeless shakespeare.txt.tl
password: <enter dummy pass>
```
6. We can forcefully set edi to the timestamp we got from GDB using the set command, and then let it continue execution.
```
Breakpoint 1, 0x00000000004017a7 in decrypt ()
(gdb) set $edi = 1588924887
(gdb) continue
Continuing.
error: checksum failed (wrong password?)
[Inferior 1 (process 5685) exited normally]
```
7. The checksum was wrong. However, consider that the file was likely last modified _after_ the call to `time(0)`. The encryption isn't super fast - it takes roughly half a second on my system. If we try a few nearby times, we can find one that works - 1588924886.
```
(gdb) set $edi = 1588924886
(gdb) continue
Continuing.
[Inferior 1 (process 5748) exited normally]
(gdb) quit
$ cat shakespeare.txt | grep ATLASSIAN
    ATLASSIAN{0ut_d4Mn3d_fL4g!_OUt_1_s4Y!}--One: two: why,
```


### Flag
`ATLASSIAN{0ut_d4Mn3d_fL4g!_OUt_1_s4Y!}`
</details>
