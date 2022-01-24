s = "Om  Shanti  777"
d=l=len=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
    len=len+1
print("Letters", l, "Digits", d, "Length", len)

#Letters 8 Digits 3 Length 15