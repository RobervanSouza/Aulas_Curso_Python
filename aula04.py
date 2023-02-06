import requests
urls = "https://www.globo.com/"
r = requests.get(urls)
print(r.text)
 