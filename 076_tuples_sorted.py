st = {'TOS': 3, 'TNG': 7, 'DSN': 7, 'Voyager': 7, 'Enterprise': 4}
s = sorted(st.items())
print(s)

for k, v in sorted(st.items()):
    print(k, v)
