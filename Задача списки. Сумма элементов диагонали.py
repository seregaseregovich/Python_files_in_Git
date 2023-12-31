''' Задача.
Реализовать функцию, которая находит сумму элементов
на главной диагонали матрицы размерности MхM, и сумму
элементов на противоположной диагонали матрицы. '''


import random


def fun1(lst, m):
    n = 0
    while m >= 0:
        n += lst[m][m]
        m -= 1
    return n


M = 5
lst1 = [[random.randint(0, 9) for i in range(M)] for j in range(M)]
for i in lst1:
    print(i)
print()

N = fun1(lst1, M-1)
print(N)
