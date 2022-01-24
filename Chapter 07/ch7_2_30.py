def counter(name, to_find="an"):
    c = name.count(to_find)
    print("{} has {} {}".format(name, c, to_find))
counter("Mississippi","is")