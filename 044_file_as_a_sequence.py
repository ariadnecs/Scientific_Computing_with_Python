file = open('star_trek.txt')
count = 0

# for each line in the file handle file
for st in file:
    # counting lines in a file
    count = count + 1
    print('line count: ', count, st)


