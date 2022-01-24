def in_both(wd1, wd2):
    common = []
    for c in wd1:
        if c in wd2:
            common.append(c)			
    return sorted(common)

print(in_both('online', 'offline'))