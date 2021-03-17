# Which will never print regardless of the value for x?
x = int(input('Enter a number: '))

if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')
