def power(integer1, integer2=3):
    result = 1
    for i in range(integer2):
        result = result * integer1

    return result
print(power(3)) 
print(power(3,2))