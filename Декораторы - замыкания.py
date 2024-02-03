'''   ЗАМЫКАНИЯ В PYTHON   '''

# ПРИМЕР 1
# =============================================


def say_name(name):
    def say_bye():
        print('Dont say me goodbye, ' + name + '!')

    return say_bye


a1 = say_name('Sergei')
a2 = say_name('Python')
a1()
a2()


# ПРИМЕР 2.1
# =============================================
# Пример создания счетчиков обращения к функции
# (независимых друг от друга)


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step


c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1())
print(c1(), c2())
print(c1(), c2())
print(c1())
print(c1(), c2())


# ПРИМЕР 2.2:
# =============================================
# Пример создания счетчиков обращения к функции
# (независимых друг от друга) с использованием декоратора

def av_n(func):
    count = 0

    def wrapper(*ag, **kg):
        nonlocal count
        count += 1
        res = func(*ag, **kg)
        return res, count

    wrapper.__name__ = func.__name__
    return wrapper


@av_n
def mult(a, b):
    return a * b


s = mult(3, 5)
w = mult(3, 5)
d = mult(3, 5)
x = mult(4, 5)
r = mult(4, 5)
print(f'Функция {mult.__name__} вызывалась {r[1] - 1} раз(а).')
print(f'Результат выполнения функции - {s[0]}.')


# ПРИМЕР 3
# =============================================
# Пример создания функции для удаления
# ненужных символов в начале и конце строки


def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" -!?,.;")
print(strip1(" hello sfgsfg !.. "))
print(strip2(" hell osfg  sfg!.    .;?  ?.. "))


# https://www.youtube.com/watch?v=sJF7OMNgLUs&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=44


# ПРИМЕР 4:
# =============================================

# Пример с замыканием, в котором реализовано
# вычисление среднего арифметического значений
# переданных в функцию чисел.


def av_n():
    num = 0
    sum = 0

    def wrapper(n):
        nonlocal num, sum
        num += n
        sum += 1
        return num / sum

    return wrapper


a = av_n()
b = a(5)
b = a(4)
b = a(4)
b = a(4)
print('Среднее арифметическое переданных чисел равно', b)


