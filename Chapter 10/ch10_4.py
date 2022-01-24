breakfast = set('Parantha')
dinner = set('Rice')
print(breakfast–dinner)

# - will return the resulting set which has elements of the left-hand set with all elements from the right-hand set removed
# difference function is used in newer version

breakfast = set('Parantha')
dinner = set('Rice')
print(breakfast.difference(dinner))