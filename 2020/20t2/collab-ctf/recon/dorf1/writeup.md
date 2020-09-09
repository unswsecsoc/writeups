# dorf1

## Authors
* Abiram Nadarajah (@abiramen)

## Category
* Recon

## Description
hey there. ceo of [dorf](https://dorf-syd.web.app) here again. 
we've got a good team, but i had to fire our frontend dev because he really wasn't getting much done (i mean, lazy to the point of using a bootstrap template? really???), and he was posting tweets that i found to be inappropriate.
i think i've done a good job of hiding any traces of him from anyone that searches for our website, but could you pls pls pls make sure i did a good job? it would be a shame if someone managed to find his tweets. thanks :)

## Difficulty
* easy

## Points
50

## Solution
<details>
<summary>spoiler</summary>

### Idea
Looking for secrets in robots.txt, and inspecting page source

### Walkthrough
1. Paying attention to 'hiding traces of him from anyone that searches', check robots.txt
2. Visit the hidden path `/r0br0bsl3g4cy.html`
3. Identifying that there seems to be invisible information, use inspect element to find an invisible image linking to a twitter page.
4. Visit the twitter page - the flag is in a tweet.

### Flag
`FLAG{b33p_b00p_i_am_n0t_a_b0t}`
</details>
