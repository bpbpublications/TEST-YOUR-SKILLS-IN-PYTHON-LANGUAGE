import collections
person = collections.namedtuple('person', ['name', 'age', 'gender'])
p1=person('Gauri','45','F')
print(p1.age, '  ', p1.gender)


# 45   F