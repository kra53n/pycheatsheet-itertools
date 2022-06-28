import itertools

seq = 'авдпр'
without_repeat = tuple(itertools.combinations(seq, 4))

for idx, elem in enumerate(itertools.product(seq, repeat=4), 1):
    if 'а' not in elem and elem in without_repeat:
        print(idx, elem)
        break
