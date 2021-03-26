smallest_so_far = 100
print('Before loop',smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)