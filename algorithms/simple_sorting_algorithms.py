def insert_sort(arr):
    """
    Пробегает по массиву чисел, сравнивает рядом лежащие их меняет местами, если один больше другого.
    :param arr: массив чисел.
    :return: отсортированный массив.
    """
    for i in range(1, len(arr)):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr


def choice_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


array = [5, -2, 9, -2.15, 5.2, -99]
print(insert_sort(array))
array = [5, -2, 9, -2.15, 5.2, -99]
print(choice_sort(array))
