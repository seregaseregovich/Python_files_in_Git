# Найти сумму первой и последней цифры числа
# VARIANT 1
n = int(input("Input number, please: "))
an = n % 10
x = 0
print()
while n != 0:
    a1 = n % 10
    n = n // 10
s = a1 + an
print(s)

# VARIANT 2
n = input("Input number, please: ")
s = int(n[0]) + int(n[-1])
print(s)
