n = int(input("Input the integer number: "))
while n != 0:
    for x in range(0, n):
        a = 2 ** x
        if a == n:
            print("YES")
            break
    if a != n or n == 0:
        print("NO")
    n = 0
    n = int(input('Введите следующее число. \nЕсли хотите выйти - введите "0"' ))
    continue

