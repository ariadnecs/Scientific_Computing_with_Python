word = str(input('Enter some word: ')).lower()

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas...')