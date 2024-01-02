'''   ЗАМЫКАНИЯ В PYTHON   '''

# ПРИМЕР 1
# ========================


def say_name(name):
    def say_bye():
        print('Dont say me goodbye, ' + name + '!')

    return say_bye


a1 = say_name('Sergei')
a2 = say_name('Python')
a1()
a2()


# ПРИМЕР 2
# ========================
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


# ПРИМЕР 3
# ========================
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
