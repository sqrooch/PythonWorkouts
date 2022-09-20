someList = [1]
someList[:0] = [2, 3, 4]
print(someList)

someList[len(someList):] = [5, 6, 7]
print(someList)

someList.extend([8, 9, 10])
print(someList)

someList = ['abc', 'ABD', 'aBe']
someList.sort()
print(someList)

someList.sort(key=str.lower)  # Сортирует список на месте.
print(someList)

someList = ['abc', 'ABD', 'aBe']
someList = sorted(someList, key=str.lower)  # Возвращает новый список.
print(someList)

someList = ['abc', 'ABD', 'aBe']
someList = sorted([x.lower() for x in someList])  # Возвращает новый список и трансформирует элементы списка.
print(someList)

someList = list(reversed(someList))  # Делает реверс списка. Принцип такой же, как у sorted, но помещена в list().
print(someList)

someList = ['Already', 'got', 'one']
someList[2:] = []  # Срез удаляет элементы...
print(someList)
someList[1] = []  # ...но вставка по индексу заменяет элемент пустым списком.
print(someList)

# Способы копирования списков:
someList2 = someList[:]
someList3 = list(someList)
someList4 = someList.copy()
