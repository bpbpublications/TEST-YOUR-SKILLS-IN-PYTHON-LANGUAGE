with open('myfile.bin', 'wb') as fl:
    text = 'You are amazing!'
    fl.write(text.encode('utf-8')) 
    
with open('myfile.bin', 'rb') as fl:
    data = fl.read(128)
    text = data.decode('utf-8') 
print(text)
