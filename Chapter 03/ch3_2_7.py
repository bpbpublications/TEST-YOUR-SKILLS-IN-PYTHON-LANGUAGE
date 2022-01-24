import re
patterns = 'ab*?'
if re.search(patterns,  "bc"):
    print('Starts with a')
else:
    print('Does not start with a')

#Does not start with a