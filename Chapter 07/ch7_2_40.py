def in_both(list1, list2):
    common = []
    for c in list1:
        if c in list2:
            if c not in common:
                common.append(c)			
    return (common)

print(in_both([1,2,5,5,3], [1,5,7]))

# [1,5]