# СПОСОБ 1:
#
# Определения скорости работы ФУНКЦИИ.
# Делает Number проходов по функции и высчитывает
# среднеарифметическое время работы функции.
import timeit


def condition_1():
    a = 1 + 2 + 3
    b = 1 + 2 + 4 * 6 * 9
    a = 1 + 2 + 3
    b = 1 + 2 + 4 * 6 * 9
    a = 1 + 2 + 3
    b = 1 + 2 + 4 * 6 * 9


def condition_2():
    a = 1 + 2 * 3


execution_time_1 = timeit.timeit(condition_1, number=1000)
print(f'Время выполнения : {execution_time_1} секунд')

execution_time_2 = timeit.timeit(condition_2, number=1000)
print(f'Время выполнения : {execution_time_2} секунд')


# СПОСОБ 2:
import datetime

datetime.datetime.now()
datetime.datetime(2022, 4, 14, 7, 45, 23, 151979)
a = str(datetime.datetime.now().date())
print(a[8:], a[5:7])
print(a[0:4])
# '2022-04-14'
b = str(datetime.datetime.now().time())
print(b[:8])
# '07:46:49.077626'

# Программа для определения скорости вып.программы
# ===============================================.

from timeit import default_timer as timer

start = timer()

# ТЕКСТ ПРОГРАММЫ

end = timer()
print("Time taken:", end - start)

# Еще способ определения скорости вып.программы
# ===============================================.

import time

t_1 = time.time()

t_2 = time.time()
print(round((t_2 - t_1), 13), 'сек', end='\n\n')

# Программа для вывода численных значений
# с периодом в 1 секунду (таймер задержки)
# =========================================

import time
import random

while True:
    for i in range(60):
        print(i)
        time.sleep(1)


# Пример проверки быстродействия разных форматированных строк
# ====================================================


from timeit import timeit


for s in ('f"{x} {y}"', '"{} {}".format(x, y)', 'x+" "+y', '"%s %s" % (x, y)'):
    print(timeit(s, 'x, y = "Hello", "World"', number=1000000), s)

# 0.06373529997654259 f"{x} {y}"
# 0.20435980008915067 "{} {}".format(x, y)
# 0.1529691000469029 x+" "+y
# 0.0793306000996381 "%s %s" % (x, y)
#
# F-строки самые быстрые.
