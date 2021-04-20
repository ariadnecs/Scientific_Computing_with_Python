import urllib.request
from urllib import request, parse, error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print(count)
