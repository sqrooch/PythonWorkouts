print(2 / 5, 2 / 5.0)
print(2 // 5, 2 // 5.0)

S = 'ham'
print('eggs' + S)
print(S[:0:-1])
print('green %s and %s' % ('eggs', S))
print('green {1} and {0}'.format('eggs', S))

L = [1, 2, 3] + [4, 5, 6]
print(L, L[:0])

print(([1, 2, 3] + [4, 5, 6])[2:4])
print(L.index(4))

print({'a': 1, 'b': 2}['b'])

d = {'x': 1, 'y': 2, 'z': 3}
d['w'] = 4
print(d, d['x'] + d['w'])
d[(1, 2, 3)] = 4
print(d)
print([[]], ['', [], (), {}, None])

someList = [1, 2, 3]
sl = someList[:]
print(someList is sl)
