from bs4 import BeautifulSoup
from urllib import request, parse, error

url = input('Enter - ')
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('bref', None))
