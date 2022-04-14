import itertools


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = itertools.groupby(iterable)
    print(*g)
    first = next(g, True)
    second = not next(g, False)
    print(f'first: {first}\tsecond: {second}')
    return first and second


def unique_justseen(iterable, key=None):
    """List unique elements, preserving order. Remember only the element just seen."
    unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    unique_justseen('ABBCcAD', str.lower) --> A B C A D
    """
    #res = map(next, itertools.groupby(iterable, key))
    #print(res)
    #for i in itertools.groupby(iterable, key):
    #    print(i)
    #return res
    res = [i[0] for i in itertools.groupby(iterable, key)]
    print(res)
    #print(list(itertools.compress(iterable, res)))


( unique_justseen(map(int, 'ABCcd'), lambda x: 1 == x ))
