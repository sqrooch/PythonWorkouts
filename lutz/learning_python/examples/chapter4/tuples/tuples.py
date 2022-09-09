T = (1, 2, 3, 3, 4)
print(T)
print(T + (5, 6))
print(T)
print(T[-1])
print(T.index(3))
print(T.count(3))
T = (2,) + T[1:]
print(T)

T = "spam", 3.14, [0, 1, 2]
print(T)
print(T[1], T[2][1])
