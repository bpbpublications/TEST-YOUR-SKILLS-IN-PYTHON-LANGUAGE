odd_even_list = ["Even" if i%2==0 else "Odd" for i in range(7)]
print(odd_even_list)
odd_even_list = [str(i) + '=Even' if i%2==0 else str(i) + "=Odd" for i in range(7)]
print(odd_even_list)

# number with even or odd displayed for numbers from 0 to 6