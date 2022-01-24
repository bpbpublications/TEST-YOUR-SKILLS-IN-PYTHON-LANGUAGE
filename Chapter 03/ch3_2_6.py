import re
patterns = 'ab*?'
if re.search(patterns,  "abc"):
    print('Starts with a')
else:
    print('Does not start with a')

#Starts with a