import re


file = open('star_trek.txt')

for line in file:
    line = line.strip()
    if re.search('^Star Trek.*:', line):
        print(line)
