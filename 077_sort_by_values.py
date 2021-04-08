st = {'TOS': 3, 'TNG': 7, 'DSN': 7, 'Voyager': 7, 'Enterprise': 4}
tmp = list()
for k, v in st.items():
    tmp.append((v, k))

print(tmp)
print('Sorted: ', sorted(tmp))

tmp = sorted(tmp, reverse=True)
print('Sorted reverse: ', tmp)


