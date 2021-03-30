from gettext import find
count = 0
founded = 0
text = open('star_trek.txt')
for line in text:
    var = line.find('Star Trek')
    if var == -1:
        count += 1
    else:
        founded += 1
        print(founded, line, end='')

print(f'\nNot found "Star Trek" in {count} lines')
