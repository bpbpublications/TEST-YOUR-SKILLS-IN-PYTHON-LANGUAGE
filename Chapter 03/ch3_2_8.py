import re
charRe = re.compile(r'[^a-zA-Z0-9.]')
s=charRe.search("BCDEFabcdef123450")
print(not(s))

#True