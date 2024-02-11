# Предпочтительный способ открытия файлов:
# ========================================

# ВАРИАНТ 1:
try:  # Проверяет наличие ошибок в работе с файлом.
    try:  # Проверяет наличие ошибок в пути или наличии файла.
        with open('abb.txt', 'r') as file:
            print(file.readline())
    except FileNotFoundError:
        print("Check filename or path to the file!")
except:
    print('Mistake has been made!')


# ВАРИАНТ 2 (упрощенный):
try:
    with open('abb.txt', 'r') as file:
        print(file.readline())
except FileNotFoundError:
    print("Check filename or path to the file!")

#