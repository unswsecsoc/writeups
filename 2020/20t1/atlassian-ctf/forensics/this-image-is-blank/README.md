# this image is blank

## Authors
* Matthew Turner (@DeadlyFugu)

## Category
* Forensics

## Description
Nothing to see here, just a blank image.

## Difficulty
* easy

## Points
50

## Hints
[1/3] how would you describe blank?
[2/3] what color is blank?
[3/3] there's a blank inside blank.

## Files
* blank.png: A white image with a message hidden within.

## Solution
<details>
<summary>spoiler</summary>

### Idea
The flag is split into three parts, each hidden with a different steganography
technique. First part is in metadata, second is in paletted colors (palette
contains two whites), and third is another image appended.

### Walkthrough
Walkthrough by: @Choco3 of 1thread

Image is blank. Yeah no.

First thing to check is the metadata of the PNG which contain may or may not contain EXIF data chunks.
In this case we can see the first part of the key in the description metadata
`[1/3] QVRMQVNTSUFOe24w`

Alright. This tells us that there are 3 keys to be found. Where else can we find them?

The art of hiding things in images is called Steganography and is prevalant in forensic CTF's.

A simple tool to use for simple steganography is a tool called StegSolve which means you dont have to install expensive image software.
Just click through each of the planes as well as the random colourmap to find the second key.
`[2/3] dF9xdTF0M19ibDRu`

Now for the hard part. We can't see any other place to hide the third key.
However, sometimes data might be hidden in the LSB (Least Significant Bit) of each image.
Let's hexdump the image file to see if we can garner some information.

The PNG file format can be classified into a couple important parts (wiki it).
PNG which represents this file as a PNG image
IDAT which represent the actual image data
IEND which represents the end of the file's image data

We can see something strange here. There's a bunch of extra data after the IEND which wouldn't be in the file normally.
EXIFTOOLS can verify this by giving a warning about data after IEND chunk

This strange data starts with a JFIF which represents a JPEG.
What is a JPEG doing inside a PNG? Let's find out. A quick google search shows us that this data has the correct structure for a JPEG
We can use the `dd` command with the correct offset (converted to dec from hex) to extract the JPEG hex data into another file

```
xxd blank.png | grep JFIF
00001d20: 4260 82ff d8ff e000 104a 4649 4600 0101  B`.......JFIF...
dd if=blank.png of=blank_stitch.jpg skip=7459 bs=1
```

Do a stegsolve on our new JPEG to discover the third portion of the key
`[3/3] a18xdF9zMzNtNX0=`

QVRMQVNTSUFOe24wdF9xdTF0M19ibDRua18xdF9zMzNtNX0=

The equal sign at the end gives hint that this is a base64 encoded string.

Decode this online to retrieve the flag:
ATLASSIAN{n0t_qu1t3_bl4nk_1t_s33m5}

-------------------------------------------------------------------------------

TL; DR
1st portion, EXIFTool description dump
2nd portion, stegsolve random colourmap the PNG
3rd portion, hexdump shows trailing data after PNG IEND, JFIF suggest jpeg.
Extract jpeg into another binary using dd with appropriate byte jump.
run stegsolve again on resulting jpeg file

Combine them into an obvious base64 encoded string which decodes to the flag.

### Flag
`ATLASSIAN{n0t_qu1t3_bl4nk_1t_s33m5}`
</details>
