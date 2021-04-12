import re

file = open('star_trek.txt')

for line in file:
    line = line.strip()
    # Regular expressions ^ .+ greedy matching, picks the longer one in 'line'
    find = re.findall('^Star.+:', line)
    print(find)
