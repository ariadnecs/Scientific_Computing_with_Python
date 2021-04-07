counts = dict()
names = ['Picard', 'Picard', 'Troi', 'Riker', 'Data', 'Riker', 'Picard', 'Data', 'Troi', 'Tasha', 'La Forge', 'Worf', 'Dr. Beverly Crusher']
for name in names:
    # if name in counts:
    #     x = counts[name]
    # else:
    #     x = 0
    # x = counts.get(name, 0)
    counts[name] = counts.get(name, 0) + 1

print(counts)
