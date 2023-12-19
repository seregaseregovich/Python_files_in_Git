def countdown(n):
    print("Обратный отсчет")
    while n > 0:
        yield n
        n -= 1  # если сделать "+",


# то будет отсчитывать от 500 в сторону увеличения
x = int(input("Enter the integer number: "))
for i in countdown(x):
    print(i)
