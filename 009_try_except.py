astr = 'Hello bob'
try:  # when the first conversion fails - it just drops into the except: clause and the program continues.
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)  # when the second conversion succeeds - it just skips the except:
# clause and the program continues.

