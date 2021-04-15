import re
file = open('mbox-short.txt')
numlist = list()

for line in file:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum: ', max(numlist))
