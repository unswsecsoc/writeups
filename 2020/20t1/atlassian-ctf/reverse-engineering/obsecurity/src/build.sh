# cleanup
rm prog.bin caa2 obsecurity.zip

# make prog.bin
python3 asm.py

# make caa2 binary
cc caa2.c -o caa2

# make zip
zip obsecurity.zip caa2.c caa2 prog.bin
