text = 'X-DSPAM-Confidence:    0.8475'
stext = text.split()

for n in stext:
    try:
        ftext = float(n)
        print(ftext)
    except:
        continue



