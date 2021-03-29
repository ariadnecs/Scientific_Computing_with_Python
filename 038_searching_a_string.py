series = 'Star Trek Voyager'
pos = series.find('Trek')
# print position
print(pos)
print(series.upper())
print(series.lower())
not_found = series.find('Wars')
# if the substring is not found, find() returns -1
print(not_found)
if not_found == -1:
    print('The substring is not found.')
