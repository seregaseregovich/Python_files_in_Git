#  Программа  для удаления дубликатов в списке.
#  Результат - в новом списке

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)

