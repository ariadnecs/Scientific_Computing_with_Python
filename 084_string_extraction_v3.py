import re

file = open('mbox-short.txt')
count = 0
for line in file:
    line = line.strip()
    if line.startswith('From') is False:
        continue
    find = re.findall('^From (\S+@\S+)', line)
    if len(find) == 0:
        continue
    print(find)
