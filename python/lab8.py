from bs4 import BeautifulSoup
import requests, re

website = requests.get('https://www.target.com/sl/fields-ertel/1091')
soup=BeautifulSoup('\n'.join(website.text.splitlines()), 'lxml')

for x in soup.find_all('a'):
    if('Cincinnati' in x.text):
        print(x.string)
        break