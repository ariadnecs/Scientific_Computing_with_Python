text = open('star_trek.txt')
for line in text:
    line = line.strip()
    if line.startswith('Star Trek'):
        print(line)
        # print(line, end='')
