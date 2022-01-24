text = "Hello 1 2 3&"
digit=0
alpha=0
space=0
for c in text:
    if c.isdigit():
        digit= digit+1
    elif c.isalpha():
        alpha=alpha+1
    elif c.isspace():
        space+=1
    else:
        pass
print("Digits:", digit, "Alphabets:",alpha, "Spaces:", space)


# Digits:3 Alphabets:5 Spaces:3