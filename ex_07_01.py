fname = input('Enter file name: ')
fh = open(fname)

for line in fh:
    up = line.upper().strip()
    print(up)
