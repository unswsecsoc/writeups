# flag pics

## Authors
* Matthew Turner (@DeadlyFugu)

## Category
* Misc

## Description
pls help!! i wrote a progam in microsoft studio 2010 to encrypt images (NOT VIRUS jsut hide files from mom) and now i cant view my flag pics!! can you get back my flags? i attach a zip of all files, i kno my encryption is very advance but maybe u can figure it out? thank uuu <3

## Difficulty
* easy

## Points
50

## Solution
<details>
<summary>spoiler</summary>

### Idea
A bunch of images which have been 'encrypted' are provided, as well as
the program used to encrypt them. Careful inspection of the program
will reveal that it's not really encrypting them - it's actually
corrupting them. Thankfully, we have a backup of the images before they
were encrypted available - in the Windows XP thumbnail cache!

### Walkthrough
1. Locate the .thumbs.db file (usually it wouldn't start with a dot,
   but then it wouldn't be hidden on unix machines)
2. Use a tool to dump the contents (various utilities for this are
   available, such as python scripts. I personally used https://thumbsviewer.github.io/)
3. Sorting the image thumbnails by order, each will contain one letter of the flag.

### Flag
`ATLASSIAN{wA1t_M0m_i_c4n_3xPLa1n}`
</details>
