def f7():
    for v in range(8):
        if v % 3 == 0 and v % 5 == 0:
            print("PythonPy")
            continue
        elif v % 3 == 0:
            print("Python3")
            continue
        elif v % 5 == 0:
            print("Python5")
            continue
        print(v)

f7()