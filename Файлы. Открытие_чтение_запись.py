# Предпочтительный способ открытия файлов:
# ========================================

# ВАРИАНТ 1:
try:  # Проверяет наличие ошибок в работе с файлом.
    try:  # Проверяет наличие ошибок в пути или наличии файла.
        with open('abb.txt', 'r') as file:
            print(file.readline())  # Вывод одной строки: Hello, hello, hello.
    except FileNotFoundError:
        print("Check filename or path to the file!")
except:
    print('Mistake has been made!')


# ВАРИАНТ 2 (упрощенный):
try:
    with open('abb.txt', 'r') as file:
        print(file.readlines())
        # ['Hello, hello, hello.\n', 'Hello, hello, hello.\n']
        # При наличии нескольких строк выводится в виде списка.
except FileNotFoundError:
    print("Check filename or path to the file!")

#