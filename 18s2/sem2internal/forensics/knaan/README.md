# K'naan't get enough

## Author
Evan

## Difficulty
Easy

## Description
My friend Zain sent me this song, It's terrible and I can't recall why he would
send it to me.

## Hint
Oh It must be for next week's event

## Files
- KNAAN - Wavin Flag (Coca-Cola Celebration Mix).mp3

## Hosting
Static hosting.

## Solving
View lyrics of id3v2 metadata.
e.g.
`mid3v2 --list-raw KNAAN\ -\ Wavin\ Flag\ \(Coca-Cola\ Celebration\ Mix\).mp3`

## Creating
1. `python3.6 -m pip install --user mutagen`
2. `python3.6 lyrics.py KNAAN\ -\ Wavin\ Flag\ \(Coca-Cola\ Celebration\ Mix\).mp3 lyrics.txt`

## Flag
`flag{l3t5_6e7_1yric4l!}`

