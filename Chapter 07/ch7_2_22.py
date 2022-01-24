def func(n):
  return lambda a : a * n

mydoubler = func(5)
print(mydoubler(10))