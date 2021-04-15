import re
file = open('star_trek_series.txt')

for line in file:
    line = line.strip()
    # ':([^ ].*)' from the colon to the end
    serie = re.findall(':([^ ].*)', line)
    print(serie)
