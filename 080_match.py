import re

file = open('star_trek.txt')

for line in file:
    line = line.strip()
    # Regular expressions: ^ \S +
    # Will show only television series because the movies are organized with whitespace and roman numbers
    if re.search('^Star Trek\S+', line):
        print(line)
