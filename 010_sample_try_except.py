rawstr = input('Enter a positive number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
elif ival == 0:
    print('This is a neutral number')
else:
    print('Invalid Option!!!')