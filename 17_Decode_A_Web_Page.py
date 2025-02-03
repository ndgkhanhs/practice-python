import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

for i in soup.find_all('p',{'class':'indicate-hover css-91bpc3'}):
    print(i.text)

for i in soup.find_all('p',{'class':'indicate-hover css-1gg6cw2'}):
    print(i.text)