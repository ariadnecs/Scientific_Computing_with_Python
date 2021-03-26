largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None and smallest is None:
        smallest = fnum
        largest = fnum
    if smallest > fnum:
        smallest = fnum
    if largest < fnum:
        largest = fnum

print("Maximum is", int(largest))
print('Minimum is', int(smallest))
