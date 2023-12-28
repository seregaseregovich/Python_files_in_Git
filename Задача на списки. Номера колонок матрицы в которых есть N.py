'''Задача.
Программа принимает число N (в диапазоне от 0 до 9).
Реализовать функцию, которая определяет, какие столбцы
имеют хотя бы одно такое число, и какие не имеют. '''

import random


def fun1(lst, n):
    lst_res = [i for i, j in enumerate(lst) if j == n]
    return lst_res


lst1 = [[random.randint(0, 9) for i in range(12)] for j in range(3)]
for i in lst1:
    print(i)
print()

N = 4
set1 = set()
for i in lst1:
    set1.update(fun1(i, N))
lst_res1 = [i + 1 for i in set1]
lst_res2 = [i for i in range(13) if i not in lst_res1]
print('Columns, including N: ', lst_res1)
print('Other columns: ', lst_res2)
