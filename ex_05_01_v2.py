total = 0
count = 0
while True:
    user = input('Enter a number: ')
    if user == 'done':
        break
    try:
        fuser = float(user)
    except:
        print('Invalid input! Try again.')
        continue
    total = total + fuser
    count += 1

print('Sum: ', total)
print('Count: ', count)
print('Average: ', total / count)
