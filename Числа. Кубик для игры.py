from random import uniform
n = input()
while n == "":
    n = round(uniform(0.5, 6.5))
    print(n)
    n = input()
    if n != "":
        break

