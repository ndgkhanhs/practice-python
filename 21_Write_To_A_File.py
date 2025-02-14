import requests
from bs4 import BeautifulSoup
import textwrap

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")

name_file = input("Enter name of text file: ")

with open((name_file+'.txt'), 'w', encoding="utf-8") as open_file:

    for i in soup.find_all('h1',{'class':'BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentHeaderHed-NCyCC iUEiRd jTFuBo gydgrM'}):
        open_file.write(i.text + "\n")

    for i in soup.find_all('p'):
        open_file.write(i.text + "\n")