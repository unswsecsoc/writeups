# Free RSS

## Authors

* todo

## Category

* web

## Tags

_web_

## Description

I've found a site that lets you subscribe to RSS feeds for free! They're even working on their own RSS hosting system, although its not avaliable yet...

## Difficulty

* medium

## Points

200

## Hints

1. `RSS is just a xml format`

## Files

_None_

## Setup

* Run the provided docker file

## Solution

_Code can be found in `solve.py`_

### Summary

This challenge involves perform a SSRF in order to access internal services. Following that we can use xxe in order to read off the file system.

#### Discovery

By navigating to `/robots.txt` we find a reference to a `/fileserver` route. Based on this route we learn of a service running on internal port 8000.

#### SSRF

The add a feed menu exposes to use the option to specify a url to fetch as well as the http method, and data to use to fetch it. We initially try pointing this to localhost:8000 but are rejected saying that only apple urls are allowed.

By doing some research we find the existance of `mail.apple.com.co` domains which resolve to localhost (127.0.0.6). We can simply use this domain in place of localhost and reach 8000.

#### File upload

Once we have SSRF we are able to interact with the fileserver. The first thing that is provided is a token. We can add this token onto our request as `http://mail.apple.com.co:8000/?token=<provided token>`.
When we request the page again we get no information. We can then try to fuzz other routes, and it turns out any arbitrary route allows for file upload. Namely `http://mail.apple.com.co:8000/something?token=<token>`
informs us that we can PUT files. We can then change the request value from `GET` to `PUT` (even though the option does not exist in the drop down we can simply add it).

#### XXE

Once we can put files into the remote server, we need a way of reading files. As RSS is a xml based protocol, we might consider exploiting the xml parser with XXE. We can hence place a malicious xml file (see malicious.xml) onto the webserver and get that from the rss application.

This gives us arbitrary file read.

### Flag

`ATLASSIAN{F14G_r3TR13vAl_ANd_s3ARCh_Sy5t3m}`