largest = -1
print('Before the loop: ', largest)
for large in [5, 2, 45, 98, 55, 100, 151, 150, 258]:
    if largest < large:
        largest = large
        print('After the loop: ', largest)

