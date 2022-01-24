def in_both(wd1, wd2):
    common = []
    for c in wd1:
        if c in wd2:
            if c not in common:
                common.append(c)			
    return (common)

print(in_both('online', 'offline'))

#[‘o’, ‘n’, ‘l’, ‘i’, ‘e’]