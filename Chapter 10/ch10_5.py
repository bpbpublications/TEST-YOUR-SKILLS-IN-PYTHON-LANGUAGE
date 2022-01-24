breakfast = set('Parantha')
dinner = set('rice')
print(breakfast–dinner)

# - will return the resulting set which has elements of the left-hand set with all elements from the right-hand set removed
# difference function is used in newer version
# {'t','n','h','P', 'a'}

breakfast = set('Parantha')
dinner = set('rice')
print(breakfast.difference(dinner))

# {'t','n','h', 'P', 'a'}