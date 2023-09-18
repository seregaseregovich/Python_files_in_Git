d = int(input("Введите сумму вклада: "))
p = int(input("Введите процент вклада: "))
L = int(input("Введите предельную сумму: "))
y = 0
while d <= L:
    y = y + 1
    d = d + (d * (p / 100))
    #d = round(d)
print(y)
d = d + (d * (p / 100))
d = round(d, 2)
print(d)
