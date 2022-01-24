import re
patterns = '[A-Z]+[a-z]+$'
if re.search(patterns, "Anuradha"):
    print('Found a match!')
else:
    print('Not matched!')

#Found a match!