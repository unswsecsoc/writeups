# dorf2

## Authors
* Abiram Nadarajah (@abiramen)

## Category
* Recon

## Description
ceo of dorf here. i hope you've finished my last two tasks! uh, i forgot my github username. havent used it in a few months - im not really in charge of development at our company. since you're here, could you find it for me? thanks. 

## Difficulty
* easy

## Points
50

## Solution
<details>
<summary>spoiler</summary>

### Idea
Looking for information connected to social media profiles

### Walkthrough
#### Intended solution
1. Look at the replies to tweets on the Twitter account found in dorf1.
2. Find Charlie's Twitter in the replies to one of the tweets.
3. Visit his page, and find a tweet containing a link to his StackOverflow account.
4. Find the link to his GitHub on his profile.
#### The solution that many people found
I made the mistake of following @torvalds and @3blue1brown using the GitHub account I made for Charlie. What I failed to realise is that Google indexes GitHub follow lists, which meant that a link to Charlie's GitHub profile was indexed in the process. Googling "charlie warner github dorf" was enough to make the GitHub profile show up.

### Flag
`FLAG{warningsfromcharlie}`
</details>
