def same_initial(word1, word2):
    if word1[0].lower() == word2[0].lower(): 
        return True
    else: 
        return False

print(same_initial('apple', 'orange'))
print(same_initial('apple', 'arrange'))