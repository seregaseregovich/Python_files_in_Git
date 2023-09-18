n = int(input("Input the integer number: "))
x = 1
while x <= n:
    x += 1
    a = n % x
    if a == 0:
        print(x)
        break
    else:
        continue

