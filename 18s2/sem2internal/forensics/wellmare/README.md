# Wellmare
A real-world incident repsonse challenge that you have to figure out how to deobfuscate the code to get the flag  
Difficulty Level: **_HIGH_**     

**[Dont forget to plant the Gist flag in one of the streams !]**    

## files
- wellmare.pdf: hand-crafted PDF with fake shellcode and obfuscated Javascript 
- details.txt: some instructions/notes of what I did to craft the PDF file  
- sauce: Source code which needs to be reedited to reflect the newest GitHub Gist link for Wellmare+ challenge
- clean.pdf: Clean version of the PDF straight from LibreOffice with nothing added
- shellcode: the shellcode that hasnt been obfuscated yet
- test.c: C wrapper test file that can compile and run the shellcode

## how2solve
1. Look through the main file and discover that some JS is being used
2. FlateDecode is also being used to obfuscate from plain sight
3. To counter this use `pdftk <input> output <output> uncompress`
4. Using the output file we can see the obfuscated shellcode
5. There are also more clues that (if you know how PDf sturcture works) ties in to the fact that JS is in one of the objects
6. The main JS object `(19 0 obj)` has to be deobfuscated by hand, so extract it and use a separate tool to do it
7. In this case I'll use `cat <obfuscated> | zlib-flate -uncompress > <out>`
8. From there do a bit of reversing to find out whats being done to the shellcode
9. After clearing up the shellcode you can either run it in a C wrapper to get the flag
10. Alternatively, if you can see that theres some hex that seems like ASCII try printing it in `Python` for the flag 


## flag
**Das flag is flag{d3crypT}**
