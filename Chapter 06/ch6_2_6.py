s = "Om Shanti 777"
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass   # do nothing statement
print("Letters", l, "Digits", d)


# Letters 8 Digits 3