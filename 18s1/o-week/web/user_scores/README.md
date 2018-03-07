# Query-db: user-scores

## Author
* zain

## Category
web

## Type
* sql injection

## Description
Check out [these awesome scores](http://35.189.24.235/)! Feel free to search for someone, be careful entering non-alphabetic characters into the search box. For some reason I can't find my friend `O'Niel` :D

## Points
40

## Hints
1. i wonder what happens when i search for my friend "o'neil"

## Files
* static/\*.css             : Just some ncie styling for the site
* templates/dickhead.html   : A error message page for if people try to sql inject drop table
* templates/index.html      : a simple html page to show results from a sql query from the user
* db.sqlite                 : a small sql server with some tables for querying through the site

## Walkthrough
The site displays a bunch of scores from the `SCORES` table but naughty zain lets
users search and just throws their text into a query without sanitising it.
The title of the challange gives away that there might be a users table.
simply doing something such as

`@' UNION SELECT * FROM USERS UNION SELECT * FROM SCORES WHERE USER LIKE '@`

makes the table display user information (which contains the flag.)

if users enter in `'` or any character that causes the sql to be malformed
they will see a sql operational error that hints them in the right direction.

the statement works because the actual code does the following

`SELECT * FROM SCORES WHERE USER LIKE '<user input>'`

So if you want to run something naughty you need to handle the first and last `'` to make them valid.

a simple `@'` handles the first one and also ensures the first statement will prob return nothing.
we can then union this with something we want to know, in our case user information.
finally we union that with something we don't care about or something that will also return something, we just need to make sure the last `'` doesn't trigger a sql operational error


## Flag
`FLAG{SQL_i5_c00l}`

## Other
### Setup
* `pip install sqlite3 flask`
* `python run.py`

