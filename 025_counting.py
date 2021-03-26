zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork += 1
    print('\033[34m', zork, '\033[m', '{:>3}'.format(thing))
print('After', zork)
