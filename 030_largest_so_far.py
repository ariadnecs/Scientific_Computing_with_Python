from random import randint
largest_so_far = -1
list_larg = []
list_num = []
print('Before loop: ', largest_so_far)
for s in range(0, 10):
    the_num = randint(0, 100)
    list_num.append(the_num)
    if the_num > largest_so_far:
        largest_so_far = the_num
        list_larg.append(largest_so_far)
    print('Largest number so far: ', largest_so_far)
print('All the numbers', list_num)
print('Largest numbers', list_larg)
print('After loop: ', largest_so_far)