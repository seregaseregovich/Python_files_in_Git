# Первый способ - с помощью enumerate:

l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = []
for i, a in enumerate(l1):
    l2 += [b for b in l1[i]]
print(l2)

# Второй способ - с помощью модуля itertools:


import itertools

ll = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
l3 = list(itertools.chain(*ll))
print(l3)


# Третий способ - традиционный
ll = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
l4 = []
for i in range(len(ll)):
    for j in ll[i]:
        l4.append(j)
print(l4)

# То же, с использованием генераторов списка

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [x for row in a for x in row]
print(c)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

