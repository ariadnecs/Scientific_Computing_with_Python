from random import randint
number = 0
larg_numbrs = []
print('\033[34mTen random numbers: \033[m')
for s in range(0, 10):
    num = randint(0, 100)
    print(num, end=' ')
    if num > number:
        number = num
        larg_numbrs.append(number)
print('\nLargest numbers \033[35m{}\033[m'.format(larg_numbrs))
print('Largest NUMBER:\033[34;40m{}\033[m'.format(number))
