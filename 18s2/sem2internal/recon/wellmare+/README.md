# Wellmare+
Recon challenge located inside the Wellmare PDF file   
`https://gist.github.com/wellllllllllllllllllll/90f09ccc47976c549c9642ca486f606e`  

## files
- setup.py: the script used to generate the Gist revisions
	- some stuff that might need to be installed: BeautifulSoup, lxml
- api\_solver.py: solver script that uses the API method to pull files down
- clone\_solver.sh: solver script that uses the cloned gist to view revisions locally (easier)

## how2solve
1. Find the URL to the GitHub Gist by working through the PDF  
2. Find a way to brute force search the gists online or clone the gist and script the revision
3. Find the correct revision with the IAM credentials  
4. Using AWS CLI, configure the client and download the flag file  

