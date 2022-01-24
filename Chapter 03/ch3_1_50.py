text = 'Teacher'
trans = {'T':'1','e':'2','a':'3','h':'4'}
table = text.maketrans(trans)
translated = text.translate(table)
print(translated)

# 123c42r