from random import randint
num = randint(0, 100)
sum = 0
print('\033[35;40mAverage of five random numbers!!!\033[m')
print('{:^30}'.format('NUMBERS:'))
for count in range(1, 6):
    num = randint(0, 100)
    sum += num
    print('\033[34m{:^3}\033[m'.format(num), end='')
    if count < 5:
        print(' + ', end='')
    else:
        print(' = {}'.format(sum))

print('\nSum = \033[35m{}\033[m \nAverage = \033[35m{:.2f}\033[m '.format(sum, sum / count))
