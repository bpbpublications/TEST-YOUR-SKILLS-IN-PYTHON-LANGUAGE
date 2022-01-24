import re
obj = re.findall(r"\w*", "Moon in the sky.")
print(obj)
for word in obj:
    obj= re.search(r"[aeiou]",word)
    if word!='' and obj==None:
	    print(word)


# ['Moon','', 'in','', 'the','', 'sky','','']
# Sky