kol = 0
s = int(input("Input digits: "))
ss = s
even = 0
odd = 0
summ = 0
maxd = 0
mind = 9
while s > 0:
    last = s % 10
    summ += last
    kol += 1
    if maxd < last:
        maxd = last
    if mind > last:
        mind = last
    if (last % 2) == 0:
        even += 1
    if (last % 2) != 0:
        odd += 1
    s = s // 10
if ss == 0:
    mind = 0
print("Number of digits", kol)
print("Odd numbers =", odd)
print("Even numbers = ", even)
print("Summ of digits =", summ)
print("Max digit is -", maxd)
print("Min digit is -", mind)




