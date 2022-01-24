with open('file1.bin', 'wb') as fl:
    fl.write(b'Hello Python')
    fl.write(b'Quiz 1:')
with open('file1.bin', 'rb') as fl:
    data = fl.read()
print(data)
