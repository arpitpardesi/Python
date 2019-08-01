import requests 
URL = "https://www.flipkart.com/"
r = requests.get(URL) 
print(r.content) 
