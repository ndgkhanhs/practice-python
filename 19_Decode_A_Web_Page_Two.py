import requests
from bs4 import BeautifulSoup
import textwrap

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

for i in soup.find_all('h1',{'class':'BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentHeaderHed-NCyCC iUEiRd jTFuBo gydgrM'}):
    print(i.text)

for i in soup.find_all('p'):
    wtext = textwrap.fill(i.text, width = 60)#, break_long_words=False, replace_whitespace=False)
    print(wtext)