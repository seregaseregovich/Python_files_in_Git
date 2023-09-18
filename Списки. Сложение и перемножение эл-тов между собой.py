# Сложение либо умножение элементов
# списка между собой (внутри того же самого списка)

#  Способ 1
l1 = [2, 6, 45, 2, 1, 33, 2, 4, 5]
a = 1
for i in l1:
    a *= i
print(a)


#  Способ 2
from functools import reduce

s = reduce(lambda a, b: a * b, l1)
print(s)

# =============================================================================
# ПРИМЕР сложения двух и более обычных списков при помощи ZIP и генератора списков

x1 = [1, 2, 3, 4, 5]
x2 = [10, 20, 30, 40, 50]
x3 = [100, 200, 300, 400, 500]
y = [a1 + a2 + a3 for a1, a2, a3 in zip(x1, x2, x3)]
print(y)

# [111, 222, 333, 444, 555]
