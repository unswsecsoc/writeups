# this script is built so that it can be called from the command-line, and not from another python file
# make your own adjustments, for my build this script will be called by an exec function in a PHP file 

import sys, urllib.parse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WebDriver:
	DOWNLOAD_DIR = '/tmp'
	
	def __init__(self, headless=True):
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--disable-extensions')
		self.options.add_argument('--no-sandbox')
		self.options.add_argument('--headless')
		self.options.add_argument('--disable-gpu')
		self.options.add_argument('--disable-setuid-sandbox')
		self.options.add_argument('--allow-running-insecure-content')
		self.options.add_argument('--ignore-certificate-errors')
		

	def __enter__(self):
		self.open()
		return self

	def open(self):
		self.driver = webdriver.Chrome(chrome_options=self.options)
		self.driver.implicitly_wait(10)
		self.driver.set_page_load_timeout(10)

	def close(self):
		self.driver.quit()

	def __exit__(self, *args, **kwargs):
		self.close()

	# set up cookie and visit insecure pages 
	def xss(self, url):
	
		flag = 'flag{congrats_heres_a_cookie_for_ya}' 

		#add cookie to browser session
		base_url = urllib.parse.urlparse(url)
		domain = "{}://{}".format(base_url.scheme, base_url.netloc)
		cookie_domain = base_url.netloc.split(':')[0]  #drop the port number 
		print("domain: {}".format(domain))
		cookie = {  'domain': cookie_domain, 'name': 'flag', 
					'path': '/', 'value': flag, 'secure': 'false'
				 }
				 
		#might have to browse to a base url first to set cookie
		self.driver.get(domain)
		self.driver.add_cookie(cookie)

		#request page 
		print("url:{}".format(url))
		self.driver.get(url)
		html = self.driver.page_source
		print(html.encode('utf-8'))
		print(self.driver.get_cookies())
		
# execute when called from command line
if __name__=="__main__":
	if(len(sys.argv) > 1): 	url  = str(sys.argv[1])
	else: sys.exit(1)
	url = urllib.parse.unquote(url)

	#add http if not present
	
	print("XSSing the URL: {}".format(url))

	with WebDriver() as driver:
		driver.xss(url)
