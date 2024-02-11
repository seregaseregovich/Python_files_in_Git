# Предпочтительный способ открытия файлов:
# ========================================

# ВАРИАНТ 1:
try:  # Проверяет наличие ошибок в работе с файлом.
    try:  # Проверяет наличие ошибок в пути или наличии файла.
        with open('abb.txt', 'r', encoding='utf-8') as file:
            print(file.readline())  # Вывод одной строки: Hello, hello, hello.
    except FileNotFoundError:
        print("Check filename or path to the file!")
except:
    print('Mistake has been made!')


# ВАРИАНТ 2 (упрощенный):
try:
    with open('D:/DATA/Работа/IT/Python_files_in_Git'
              '/abb.txt', 'r', encoding='utf-8') as file:
        print(file.readline(4))
        print(file.readline())
        file.seek()  # переводит точку считывания в нужную позицию
        print(file.tell())  # возвращает текущую позицию точки считывания текста файла
        print(file.readline(10))
        # ['Hello, hello, hello.\n', 'Hello, hello, hello.\n']
        # При наличии нескольких строк выводится в виде списка.
except FileNotFoundError:
    print("Check filename or path to the file!")
