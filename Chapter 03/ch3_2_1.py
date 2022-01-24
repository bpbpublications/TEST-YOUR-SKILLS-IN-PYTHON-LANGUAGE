import re
patterns = '[A-Z]+[a-z]+$'
if re.search(patterns, "wOnDeR"):
    print('Found a match!')
else:
    print('Not matched!')

# Not matched!