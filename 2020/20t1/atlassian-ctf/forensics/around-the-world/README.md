# Around the World

## Author
Vicknesh

## Category
Forensics

## Description
Someone stole my phone :(. The worst part is that I went on holiday to Sydney recently and now I have no pictures to remember my trip by. But then a couple days ago, a photo I took in Sydney got uploaded twice to my google drive. Could you help me find where my phone is?

## Difficulty
medium

## Points
100

## Hint
metadata is not the only way to hide something in an image

## Files
a.jpg : image file with a picture of the opera house
b.png : image file with a visually identical picture to a.jpg

## Solution
<details>
<summary>spoiler</summary>

### Idea
A question that involves both steg as well as info hidden in the metadata and some crypto elements.

### Walkthrough
1. Look at the metadata for a.jpg
2. Geotags say (40.712775, -74.005975), which is in New York, but the photo is of the Opera House so this is quite suspicious
3. the description is a base64 encoded string. Decoding the string, gives a link https://www.dcode.fr/progressive-caesar-cipher
4. b.png has information that has been stegonographically encoded using lsb. This can be decoded using https://stylesuxx.github.io/steganography/ or a tool of your choice
5. you will get a bunch of data of the form {latitude,longitude,string}. If you use the coordinates in the geotag of a.jpg’s metadata, and decode the associated string using the link in a.jpg’s description, you will get the flag

### Flag
`ATLASSIAN{Australians_aLLleTUsreJOicE__VdWpLXmtIU}`
</details>
