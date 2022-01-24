import re
charRe = re.compile(r'[^a-zA-Z0-9.]')
s=charRe.search("%12345")
print(not(s))


# False