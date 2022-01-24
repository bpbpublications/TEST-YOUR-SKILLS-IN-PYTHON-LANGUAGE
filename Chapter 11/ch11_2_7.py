def func(t1):
    m=max(t1)
    if m>100:
        print("Tuple has 3-digit values")
    elif m>10:
        print("Tuple has 2-digit values")
    else:
        print("Tuple has single-digit values")
func((1,11,13))

#Tuple has 2-digit values