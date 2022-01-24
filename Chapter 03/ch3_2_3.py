import re
patterns = 'xy+?'
if re.search(patterns,  "xzy"):
    print('Starts with x and has one y')
else:
    print('No matching')

# No matching