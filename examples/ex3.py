from itertools import accumulate


l = [1, 3, 4, 5, 10]


print(tuple(accumulate(l)))
print(accumulate(l))


a = accumulate(l)
print(next(a))
print(next(a))
