input_file = "Sandstorm.wav"
output_file = "Soundstorm.wav"
msg = "flag{m0r3_l1ke_da_rud3}"
msg = ["{0:08b}".format(ord(x)) for x in msg]
msg = "".join(msg)

with open(input_file,"rb") as f:
	data = f.read()

data = list(data)
offset = 80
for i,b in enumerate(msg):
	di = offset+i
	org = "{0:08b}".format(data[di])
	data[di] = data[di] | 1
	if b == "0":
		data[di] -= 1
	i+=1

with open(output_file,"wb") as f:
	f.write(bytes(data))
