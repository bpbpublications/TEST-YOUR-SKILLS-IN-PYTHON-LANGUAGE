import re
patterns = 'xy+?'
if re.search(patterns,  "xyz"):
    print('Starts with x and has one z')
else:
    print('No matching')

#Starts with x and has one z