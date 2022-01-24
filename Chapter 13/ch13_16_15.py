f=open('file1.txt', 'w')
f.write("First Line.\nSecond Line.")
f.close()
f=open('file1.txt')
while True:
    try:
        line=next(f)
        print(line)
    except StopIteration:
        break
f.close()
