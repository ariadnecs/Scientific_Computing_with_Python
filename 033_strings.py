fruit = 'banana'
# length
x = len(fruit)
print('Length:', x)

for n in 'banana':
    print(n, end='')

print('\n')
for letter in fruit:
    print('\033[33m{}\033[m'.format(letter.upper()), end='')

index = 0
print('\n')
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
