str1 = 'Hello'
print(str1.endswith('e', 0, 2)) 
print(str1.endswith('o', 0, 4))

#True (substring 'He' (0 to 1 index) ends with 'e')
#False (substring 'Hell' (0 to 3 index) does not end with 'o')