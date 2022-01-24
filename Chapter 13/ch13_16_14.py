f=open('file1.txt')
while True:
    try:
        line=next(f)
        print(line)
    except StopIteration:
        break
f.close()
