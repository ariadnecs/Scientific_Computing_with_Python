series = '   Star Trek   '
count = 0

for letter in series:
    if letter == ' ':
        count += 1

print('I found {} whitespaces.'.format(count))
print('Removing whitespaces at the left...')
print(series.lstrip())
print('Removing whitespaces at the right...')
print(series.rstrip())
print('Removing whitespaces at the both sides...')
print(series.strip())
