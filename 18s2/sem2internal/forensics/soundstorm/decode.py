from tqdm import tqdm
import re

input_file = "Soundstorm.wav"

with open(input_file,"rb") as f:
	data = f.read()

data = list(data)
byte = 0
c = 0
msg = ""
for b in tqdm(data):
	if c == 8:
		#print("{0:08b}".format(byte),chr(byte))
		msg += chr(byte)
		byte = 0
		c = 0
	bit = (b&1)
	# leftmost bit is now 0
	byte = (byte << 1)
	if bit != 0:
		byte = byte | bit
	c+=1

f = re.search("(flag\{[^\}]*\})",msg)
if f:
	print(f.group(1))
else:
	print("No Flag Found...")
