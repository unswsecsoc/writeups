# https://discord.gg/g2QHGQF

## Author
* Abiram

## Category
* Misc

## Description
wowie this is a powerful search function

## Difficulty
* easy

## Points
25

## Solution
<details>
<summary>spoiler</summary>

### Idea
Participants are expected to use Discord's search filters in order to speed up searching through potential results.

### Walkthrough
1. Since the flag format is known to be ATLASSIAN{}, enter ATLASSIAN in the Discord search box. Several older messages were edited to be red herrings, but one search result contains the following contents:
```
ATLASSIAN{ nice try, but the flag is actually in an image i posted to this server, so keep looking! don't worry, it'll be visible to the naked eye when you come across it. }
```
2. Using this clue, use the following search entry to narrow down results: `from: abiramen#2452 has:image`. Looking through the ~50 results at the time yields an image with the flag in plain sight.

### Flag
`ATLASSIAN{w0w_w3lc0me_t0_th3_d1sc0rd_n1ce_s3arch1ng_sk1ll5}`
</details>
