import re
file = open('star_trek_series.txt')

for line in file:
    line = line.strip()
    # '^Star.*:([^ ].*)' from the colon to the end of the line
    serie = re.findall('^Star.*:([^ ].*)', line)
    print(serie)
