someList = [0, 1, 2, 3]
someList[2] = []
print(someList)
someList[2:3] = []
print(someList)
del someList[0]
print(someList)
someList = [1, 2, 3]
del someList[1:]
print(someList)
someList = [0, 1, 2, 3]
someList[1:2] = [40, 50]  # Присваивает только последовательности, но не объект.
print(someList)

someList[1:2] = 100
print(someList)
