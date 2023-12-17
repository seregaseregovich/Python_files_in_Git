# Программа для создания имен переменных:
# ВАРИАНТ 1:
l1 = ['a', 'b']
n = 4
l2 = [f'{x}{y}' for y in range(1, n + 1) for x in l1]
print(l2)
# Результат:
# ['a1', 'b1', 'a2', 'b2', 'a3', 'b3', 'a4', 'b4']

# ВАРИАНТ 2:
lst = ['a', 'b']
lst2 = []
for i in range(1, 5):
    lst2.append(lst[0] + str(i))
    lst2.append(lst[1] + str(i))
print(lst2)
