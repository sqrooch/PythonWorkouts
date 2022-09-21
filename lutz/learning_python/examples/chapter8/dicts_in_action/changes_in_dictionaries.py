someDict = {k: v for (v, k) in zip(['a', 'b', 'c'], [1, 2, 3])}  # Включения словарей.
print(someDict)
someDict = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(someDict)

someDict = dict.fromkeys(['a', 'b', 'c'])
print(someDict)
someDict = dict.fromkeys([1, 2, 3])
print(someDict)
someDict = dict.fromkeys('spam')
print(someDict)
someDict = dict.fromkeys('spam', 0)
print(someDict)

for k in someDict:  # Нет нужны вызывать someDict.keys()
    print(k)

# Объединения представлений:
someDict = {'a': 1}
print(list(someDict.items()))
print(someDict.items() | someDict.keys())
print(someDict.items() | {('c', 3), ('d', 4)})
print(dict(someDict.items() | {('c', 3), ('d', 4)}))

someDict = {'b': 2, 'c': 3, 'a': 1}
print(someDict)
ks = someDict.keys()
print(ks)
ks = list(someDict.keys())
print(ks)
ks.sort()
print(ks)
for k in ks:
    print(k, someDict[k])

# Можно проще:
someDict = {'b': 2, 'c': 3, 'a': 1}
print(someDict)
for k in sorted(someDict):
    print(k, someDict[k])
