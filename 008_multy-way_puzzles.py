# Which will never print regardless of the value for x?
x = int(input('Enter a number: '))

if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10')
else:
    print('Something else')
