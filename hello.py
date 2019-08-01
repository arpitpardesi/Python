from bs4 import BeautifulSoup
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except urllib.error.URLError as e: ResponseData = e.reason:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
url = urlopen("http://www.google.com")

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")