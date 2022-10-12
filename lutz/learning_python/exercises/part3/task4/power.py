# L = [2**rate for rate in range(10)]
L = list(map(lambda rate: 2 ** rate, range(10)))
x = 5
if 2 ** x in L:
    print('at index', L.index(2 ** x))
else:
    print(x, 'not found')
