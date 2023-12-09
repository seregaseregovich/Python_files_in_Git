# Программа для перебора всех возможных вариантов
# расположения элементов последовательности


import itertools

a = list(itertools.permutations([1, 3, 1, 9]))
print(len(a))
