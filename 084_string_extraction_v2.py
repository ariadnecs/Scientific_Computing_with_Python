import re

x = 'Science spock@startrek.com command kirk@startrek.com communications uhura@startrek.com, medical bones@startrek.com'
y = re.findall('\\S+@\\S+', x)
print(y)

y = re.findall('^Science (\\S+@\\S+)', x)
print(y)
