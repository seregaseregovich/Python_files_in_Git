# Перевод чисел в двоичный код при помощи функции bin

a=0o101  # Восьмеричный код (0o перед кодом)
print(a)
print(type(a))
print(bin(a))  # Бинарный (двоичный) код (0b перед кодом)

#
my_int = int('1011110', 2)  # 2
print(my_int)


# Программа для перевода чисел из 10-чной в
# любую другую систему счисления (не содержащую букв)
kol = 0
s = int(input("Input number to convert (10-digit system): ")) #12345
ss = int(input("Input digit system to convert: "))
c = 0
while s > 0:
    c = s % ss
    print(c)
    s = s // ss
print("Your number in ", ss, "- digit system.")


# Перевод чисел из десятичной системы в двоичную:
# 14//
b = ""
s = ""
while s == "":
    n = int(input("Введите десятичное число для перевода: "))
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)
    s = input("Чтобы продолжить нажмите ввод.\nЧтобы выйти введите любой символ: ")
print("Вы успешно вышли из системы.")


