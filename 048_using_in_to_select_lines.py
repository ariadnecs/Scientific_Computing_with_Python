text = open('star_trek.txt')
for line in text:
    line = line.strip()
    if not 'Star Trek' in line:
        continue
    print(line)
    # if line.startswith('Star Trek'):
        # print(line)
