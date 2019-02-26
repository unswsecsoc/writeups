# Challange

given a mp3 file extract out a hidden flag

# Solution 

It was just a simple LSB challange. The way i encoded the message in is below

`encode.py`

```python
input_file = "Sandstorm.wav"
output_file = "Soundstorm.wav"
msg = "flag"
# convert message to a bit string
msg = ["{0:08b}".format(ord(x)) for x in msg]
msg = "".join(msg)

with open(input_file,"rb") as f:
	data = f.read()
# read through file from 80 onwards
# (80 is where the header ends)
data = list(data)
offset = 80
for i,b in enumerate(msg):
	# chuck the message bit in at the LSB
	di = offset+i
	data[di] = data[di] | 1
	if b == "0":
		data[di] -= 1
	i+=1

# write out hidden file. 
with open(output_file,"wb") as f:
	f.write(bytes(data))

```

So to get the hidden message simply generate a bit stream of the LSB from every byte in the file and then attempt to convert it all into text and grep for flag. 

`decode.py`

```python
# just a package that gives a progress bar
# to slow loops
from tqdm import tqdm
#regex
import re

# read all bytes
input_file = "Soundstorm.wav"
with open(input_file,"rb") as f:
	data = f.read()

data = list(data)
byte = 0
c = 0
msg = ""
# read through all bytes
for b in tqdm(data):
	# once you have 8 bits
	# form a byte. 
	if c == 8:
		msg += chr(byte)
		byte = 0
		c = 0
	# extract out a bit and add it 
	# to the gradually constructed byte
  
  # isolate last bit (bit is now 1 or 0)
	bit = (b&1)
	# leftmost bit of byte is now 0
	byte = (byte << 1)
	# see if it should be 1
	if bit != 0:
		byte = byte | bit
	# increment bit count
	c+=1
# grep for flag
f = re.search("(flag\{[^\}]*\})",msg)
if f:
	print(f.group(1))
else:
	print("No Flag Found...")
```
