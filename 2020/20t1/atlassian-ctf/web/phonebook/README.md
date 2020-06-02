# Phonebook

## Authors
* todo

## Category
* Web

## Tags
* XSS

## Description
One day I made a phone book application. After finishing I immediately realised I didn't need it
since no one talks to me anyway... :(. Anyway, go hack it.

## Difficulty
* hard

## Points
400

## Hints
N/A

## Files
* encoder.py
* solve.py
* src: Challenge Source

## Setup
1. Run the provided docker file

## Solution
<details>
<summary>spoiler</summary>

### Description
This challenge involves performing XSS, but with a extremely limited character set and file size.

Whilst technically a XSS challenge it is much a exercise in javascript.

#### Discovery
Creating a phone book we notice a global variable `c` which contains `document.cookies` and `n` which calls a notify function. We likely want to get the admin to execute `n(c)`.

#### Restirctions
We notice that we can trivially get XSS by putting `<script>` into the phonebook name selection. However, the number of characters here is limited so we cannot fit a full xss payload. We hence append a `/*` onto the end of the script to comment out everything else on the page.

We also note that every phone number is also XSSable, but the length is extremely limited (7 characters), and we cannot have `A-Za-z` or backticks. We can however have all other symbols

We can freely write javascript as long as we comment out the rest of the line. This leaves us with `*/ppp/*` 3 character payloads.

#### Building payloads
The first restriction we over come is letters. We notice we can build letters from javascript's implicit type casting. For example `''+1/0` will output the string `Infinity`, from here we get access to the letters `finty`. Infact it is possible to build up a large portion of the alphabet using only `Infinity, true, false, and [object Object]`.

From here we can construct the entire alphabet (see `encoder.py`).

#### Eval
Although we can now build payloads we still need to be able to eval them. Luckily javascript can convert strings to functions on the fly. We can do this by accessing the constructor of a constructor, which will be the `Function` type. e.g. `({})[encode('constructor')][encode('constructor')](<payload>)()` will give us executable javascript.

#### Exploit
Chaining all of this together we can then simply encode a payload for `n(c)` and eval it on the admin side. This will get us the flag in our html source code within a few minutes.

### Flag
`ATLASSIAN{1ll_0p3n_a_J1R4_t1CK3T_f0r_it}`
</details>
