M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)

col2 = [row[1] for row in M]  # собрать элементы в столбце 2.
print(col2)

col2 = [row[1] + 1 for row in M]  # собрать элементы в столбце 2 увеличенный на единицу.
print(col2)

col2 = [row[1] for row in M if row[1] % 2 == 0]  # отфильтровать нечётные элементы.
print(col2)

diag = [M[i][i] for i in [0, 1, 2]]  # собрать диагональ матрицы.
print(diag)

doubles = [c * 2 for c in "spam"]
print(doubles)

print(list(range(4)))
print(list(range(-3, 8, 3)))
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, int(x / 2), x * 2] for x in range(-4, 9, 2) if x > 0])

G = (sum(row) for row in M)
print(next(G), next(G))
print(next(G))

print(list(map(sum, M)))

print({sum(row) for row in M})
print({i: sum(M[i]) for i in range(3)})

print([ord(x) for x in "spaam"])
print({ord(x) for x in "spaam"})
print({x: ord(x) for x in "spaam"})
print((ord(x) for x in "spaam"))
