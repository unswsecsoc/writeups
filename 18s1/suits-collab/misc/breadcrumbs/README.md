# breadcrumbs

## Flavortext
I think some fictitious characters are worried for their lives and have tried to leave a message through a [trail of breadcrumbs](https://cgi.cse.unsw.edu.au/~evank/other/breadbits/start)?  

## Hint
(no hint)

## Solution

The generated folder by _gen.py_ will contain loads of files and subdirectories, but one of the files has the flag. Your task would be to follow the trail and get the flag, but nobody has time to do it by hand since there are so many. 

Either by writing a script or using a fuzzer (since the pattern is solely numeric), you can brute force the number in the URL until you eventually get the flag. 

A neat way to skip irrelevant items is to check for data-length, and issue a warning when something greater than a few bytes appears. 

## Answer
FLAG{h4n53l_&_gr3t3l}



