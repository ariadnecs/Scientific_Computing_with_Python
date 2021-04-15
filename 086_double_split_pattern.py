file = open('star_trek_series.txt')

for line in file:
    line = line.strip()
    title = line.split(':')
    print(title)
    series = title[1]
    # print(series)
    pieces = series.split(':')
    print(pieces)
