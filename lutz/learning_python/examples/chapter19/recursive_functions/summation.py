def my_sum(L):
    if not L:
        return 0
    else:
        return L[0] + my_sum(L[1:])


print(my_sum([1, 2, 3, 4, 5]))
print(my_sum([1, 2, 0, 4, 5]))
