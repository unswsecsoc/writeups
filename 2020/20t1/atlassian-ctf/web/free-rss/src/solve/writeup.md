_Code can be found in `solve.py`_

### Description
This challenge involves perform a SSRF in order to access internal services. Following that we can use xxe in order to read off the file system.

#### Discovery
By navigating to `/robots.txt` we find a reference to a `/fileserver` route. Based on this route we learn of a service running on port 8001.

#### SSRF
The add a feed menu exposes to use the option to specify a url to fetch as well as the http method, and data to use to fetch it. We initially try pointing this to localhost:8001 but are reject saying that only apple urls are allowed.

By doing some research we find the existance of `mail.apple.com.co` domains which resolve to localhost. We can simply use this domain in place of localhost and reach 8001.

#### XXE
Once we can put files into the remote server, we need a way of reading files. As RSS is a xml based protocol, we might consider exploiting the xml parser with XXE. We can hence place a malicious xml file (see malicious.xml) onto the webserver and get that from the rss application.

This gives us arbitrary file read.
