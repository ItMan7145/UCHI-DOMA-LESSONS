from math import perm

a = {1, 2, 3, 'a', 'b', 'c'}

# b = set([4, 5, 6])
c = frozenset([7, 8, 9])

# sum = a + c
a.add(c)
# a.add(c.union())
# a.union(c)

print(a)
