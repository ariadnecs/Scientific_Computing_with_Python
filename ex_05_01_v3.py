num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ').upper()
    if sval == 'DONE':
        break

    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval

print(tot, num, tot/num)
# print('All done!')
print('Done!')
