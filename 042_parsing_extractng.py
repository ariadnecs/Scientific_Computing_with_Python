data = 'Star Trek is the best franchise ever!'
atpos = data.find('the')
print(atpos)
sppos = data.find('!')
print(sppos)
truth = data[atpos:sppos+1]
print(data[:13])
print(truth)
print(data[13:37])
