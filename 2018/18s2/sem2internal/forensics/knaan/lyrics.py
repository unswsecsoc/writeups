
import sys
from mutagen import MutagenError
from mutagen.id3 import ID3, USLT, ID3NoHeaderError

try:
    tags = ID3(sys.argv[1])
except ID3NoHeaderError:
    tags = ID3()

with open(sys.argv[2], "rb") as h:
    text = h.read().decode("utf-8")
    tags.delall("USLT")
    tags.add(USLT(text=text, lang="eng", desc=""))

tags.save(sys.argv[1])