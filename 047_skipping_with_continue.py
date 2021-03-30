text = open('star_trek.txt')
for line in text:
    line = line.strip()
    if not line.startswith('Star Trek'):
        continue
    print(line)
