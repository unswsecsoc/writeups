# P@ssw@rd

## Authors
* p1gc0rn

## Category
* Forensics

## Tags
* MacOSX

## Description
I want to buy hats for Mad Hat from Alibaba, but I dont remember the password to login :( Send help!

## Difficulty
* medium
* hard

## Points
200

## Hints
1. Keychains application
2. Chain breaker

## Files
* mem.raw [800mb download here](https://drive.google.com/file/d/1-t9-2uXzVjPghOVYP_K2jYyMOYj0r82Z/view?usp=sharing)
* MacSierra_10_12_16A323x64 (profile file for volatility)

## Solution
<details>
<summary>spoiler</summary>

### Idea
Dump the login.keychain file(the base file for Keychains application) and the master keys from mem.raw. Then use chainbreaker to unlock the content of login.keychain file. The flag is encoded in base64 format.

### Walkthrough
1. Dump all the files from mem.raw
`python volatility/vol.py -f Downloads/mem.raw --profile MacSierra_10_12_16A323x64 mac_list_files > files.txt`
2. Get the vnode of login.keychain from files.txt
3. Extract the content of login.keychain
`python volatility/vol.py -f Downloads/mem.raw --profile MacSierra_10_12_16A323x64 mac_dump_file -q 0xffffff8028f0b648 -O login.keychain`
4.Find the master key for login.keychain
`python volatility/vol.py -f Downloads/mem.raw --profile MacSierra_10_12_16A323x64 mac_keychaindump`
5. Use the chainbreaker to unlock the content and find alibaba.com
`python chainbreaker/chainbreaker.py -f login.keychain-db -k 064F67E2526F2642D41D7EF2C4E3B6EDC07D36B9760635E7 | strings`
6. The flag is in the password section, encoded in base64
QVRMQVNTSUFOe2JkNzJiYzUxMjNmNWQ1NDM2NzJlNTEzYTUxYzExMDZlfQ==.

### Flag
The finding is the hash which needs wrapping with flag format.
`ATLASSIAN{bd72bc5123f5d543672e513a51c1106e}`
</details>
