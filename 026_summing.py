zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print('\033[34m{:>4}'.format(thing), '\033[m', '{:>4}'.format(zork))
print('After', zork)
