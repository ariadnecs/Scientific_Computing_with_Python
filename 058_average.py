total = 0
count = 0
while True:
    num = input('Enter a number: ').lower()
    if num == 'done':
        break
    value = float(num)
    total += value
    count += 1

average = total / count
print('Average: ', average)