#  Способ 1

import math

a = float(input("Введите количество школьников в А-классе: "))
b = float(input("Введите количество школьников в Б-классе: "))
c = float(input("Введите количество школьников в В-классе: "))
a2 = math.ceil(a/2)
print("Количество требуемых парт в А-классе:", a2)
b2 = math.ceil(b/2)
print("Количество требуемых парт в Б-классе:", b2)
c2 = math.ceil(c/2)
print("Количество требуемых парт в В-классе:", c2)
x = a2 + b2 + c2
print("Количество требуемых парт всего -", x)


#  Способ 2

import math

x = math.ceil(float(input())/2) + math.ceil(float(input())/2)\
    + math.ceil(float(input())/2)
print(x)
