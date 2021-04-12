import re

file = open('star_trek_films.txt')

for line in file:
    line = line.strip()
    # regular expressions [0-9] +
    if re.findall('[0-9]+', line):
        print(line)

    find = re.findall('[0-9]+', line)
    print(find)
