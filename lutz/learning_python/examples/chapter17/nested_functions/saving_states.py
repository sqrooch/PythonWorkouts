def f1():
    x = 88
    f2(x)  # Опережающая ссылка допустима


def f2(x):
    print(x)


f1()


def func():
    y = 4
    action = (lambda n: y ** n)
    return action


y = func()
print(y(2))

# ИЛИ

print((lambda n: 4 ** n)(2))
