# def proizvedenie(x, y, z):
#    r = (x * y) ** z
#    return(r)
#
# Пример обычного применения функции
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
# r = proizvedenie(x, y, z)
# print(r)

# Пример применения функции со списком
def summa1(a, b, c):
    return a + b + c


t1, arr = (1, 2, 3), [4, 5, 6]  # Создаем кортеж и список
print(summa1(*t1))  # Распаковываем кортеж
print(summa1(*arr))  # Распаковываем список

t2 = (2, 3)  # Создаем кортеж из двух элементов (вместо трёх)
print(summa1(11, *t2))  # Комбинируем (складываем число 1 и два числа из кортежа)


# Ещё пример применения функции со списками и кортежами
def summa2(a, b, c, d, e, f):
    return a + b + c + d + e + f


arr1, arr2 = [1, 2, 3], [4, 5, 6]
trr1, trr2 = (1, 2, 3), (4, 5, 6)
print(summa2(*arr1, *arr2))
print(summa2(*trr1, *trr2))


# Пример с использованием словаря
def summa3(a, b, c, d, e, f):
    return a + b + c + d + e + f


d1, d2 = {"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5, }
trr1, trr2 = (1, 2, 3), (4, 5, 6)
print(summa3(**d1, **d2, f=0))
print(summa3(*trr1, *trr2))
