lines=["Hello Everyone!\n", "Welcome to File Handling.\n"]
f=open("myfile.txt", "w")
f.writelines(lines)
f.close()