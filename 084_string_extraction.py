import re

file = open('mbox-short.txt')

for line in file:
    line = line.strip()
    if re.findall('@', line):
        find = re.findall('\S+@\S+', line)
        print(find)
