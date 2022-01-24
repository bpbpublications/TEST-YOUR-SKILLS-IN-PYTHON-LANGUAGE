def func(n):
  return lambda a : a * n

mydoubler = func(2)
print(mydoubler(13))