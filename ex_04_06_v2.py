def computepay(hours, rate):
    # print('In computepay', hours, rate)
    if fh > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print('Returning', pay)
    return pay


sh = input('Enter Hours: ')# string hour
sr = input('Enter Rate: ')# string rate
fh = float(sh)# float hour
fr = float(sr)# float rate

xp = computepay(fh, fr)

print('Pay:', xp)
