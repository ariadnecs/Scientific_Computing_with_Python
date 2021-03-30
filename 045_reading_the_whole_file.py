file = open('star_trek.txt')

# reading the whole file, newlines and all
inp = file.read()
print(len(inp), '\n')
print(inp[:36])
