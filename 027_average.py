count = 0
sum = 0
print('Before', sum)
for thing in [9, 41, 12, 3, 74, 15]:
    sum = sum + thing
    count += 1
    print('\033[35mQuantity of numbers: {}\033[m'.format(count), '\033[34mNumber: {:>3}'.format(thing), '\033[m', 'Sum: {:>3}'.format(sum))
print('After', sum)
print('Average = {:.2f}'.format(sum/count))
