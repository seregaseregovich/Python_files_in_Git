''' Задача.
Дана матрица MxN.
Необходимо добавить к матрице еще один столбец,
элемент в котором делает количество единиц
в соответствующей строке четным. '''


def func(lst):
    for i in lst:
        if sum(i) % 2 != 0:
            i = i.append(1)
        else:
            i = i.append(0)
    return lst


array1 = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0]
]

lst = list(func(array1))

for i in lst:
    print(i)
