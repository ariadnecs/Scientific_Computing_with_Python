counts = dict()
names = ['Picard', 'Picard', 'Troi', 'Riker', 'Data', 'Riker', 'Picard', 'Data', 'Troi', 'Tasha', 'La Forge', 'Worf', 'Dr. Beverly Crusher']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)
