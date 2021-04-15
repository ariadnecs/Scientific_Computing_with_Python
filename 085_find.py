stfirst = 'Star Trek VIII:First Contact'
beginning = stfirst.find(':')
print(beginning)
#end = stfirst.find(' ', beginning)
#print(end)

movie = stfirst[beginning+1:]
print(movie)


