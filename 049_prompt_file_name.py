fname = input('Enter the file name: ')

try:
    file = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in file:
    if line.startswith('Star Trek'):
        count += 1
print('There were', count, 'subject lines in', fname)
