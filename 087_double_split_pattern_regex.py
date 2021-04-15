import re
file = open('star_trek_series.txt')

for line in file:
    line = line.strip()
    serie = re.findall(':([^ ]*)', line)
    print(serie)
