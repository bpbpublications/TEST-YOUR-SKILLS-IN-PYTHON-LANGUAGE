def odd_values_string(str): 
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i] 
    return result

print(odd_values_string('a1b2c3d4e5f6g7h8i9'))

#abcdefghi