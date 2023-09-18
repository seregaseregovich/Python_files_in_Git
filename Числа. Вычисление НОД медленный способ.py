# Найти наибольший общий делитель (НОД) двух чисел каличный медленный способ
m = int(input("Number 1: "))
n = int(input("Number 2: "))
a = []
b = []
for x in range(m):
    x = x + 1
    ma = m % x
    if ma == 0:
        a.append(x)
for y in range(n):
    y = y + 1
    na = n % y
    if na == 0:
        b.append(y)
c = a + b
print(c) # Общие делители двух чисел в одном списке
d = []
if m > n:
    r = m
else:
    r = n
for i in range(r):
    ss = c.count(i)
    if ss > 1:
        d.append(i)
print(d) # общие делители двух чисел
print(max(d)) # наибольший общий делитель двух чисел
