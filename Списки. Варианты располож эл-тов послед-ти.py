# Программа для подсчета количества всех возможных вариантов
# расположения элементов последовательности


import itertools

a = list(itertools.permutations([1, 3, 6, 2, 4]))
print(len(a))
