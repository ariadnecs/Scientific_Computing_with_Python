import re
file = open('star_trek.txt')

for line in file:
    line = line.strip()
    find = re.findall('^Star Trek.+?:', line)
    print(find)
