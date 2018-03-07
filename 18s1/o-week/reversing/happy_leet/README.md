# Happy Leet

## Author
* kawing 
* evan

## Category
Reversing

## Type
* web
* query
* formula

## Description
Can you get leet and make the [website](https://cgi.cse.unsw.edu.au/~evank/other/happy/) happy?

## Points
30

## Hints
1. It helps to be systematic!
2. What is an ascii table? How can it help you?

## Files
* index.cgi: The Python CGI script that the website runs on.

## Walkthrough
1. User-input string is evaluated for its ascii value character by character 
2. Even characters will be added
3. Odd characters will be subtracted
4. Goal is to get the string to produce the value **1337**
5. Example solution: `~!~!~!~!~!~!~!~!~!~!~!~!~!~!~[`

## Flag
`FLAG{asc!!_what_you_d!d_there}`
