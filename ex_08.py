text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    wds = line.split()

    # print('Line: ', line)
    # print('Words: ', wds)
    # if line == '':
    #     print('Skip Blank')
    #    continue

    # Guardian pattern, a bit stronger
    # if len(wds) < 3:
    #    continue
    # if wds[0] != 'From':
    #   print('Ignore')
    #     continue

    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    
    print(wds[2])
