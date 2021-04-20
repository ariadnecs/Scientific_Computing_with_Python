import urllib.request
from urllib import request, parse, error
import ssl
from bs4 import BeautifulSoup

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags <a  > </>a>
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
