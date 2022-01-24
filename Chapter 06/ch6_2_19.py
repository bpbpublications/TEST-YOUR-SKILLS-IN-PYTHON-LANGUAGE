sentence = "for, while, do while"
word = ""
space = sentence.find(" ")
while space != -1:
    word = sentence[0:space]
    sentence = sentence[space+1:]
    print(word, sentence)
    space = sentence.find(" ")

''' output
for, while, do while
while, do while
do while

'''