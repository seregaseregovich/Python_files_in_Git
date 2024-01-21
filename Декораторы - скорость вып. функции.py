'''Декоратор test_time предназначен для проверки
или сравнения скорости выполнения функций'''

import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Time = {dt} sec')
        return res
    # Стандартный подход для сохранения имени и
    # докумментации функции.
    # ВАРИАНТ 1:
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    # ВАРИАНТ 2:
    # from functools import wraps
    # Вместо двух строчек выше (и перед
    # функцией wrapper) ввести декоратор:
    # @wraps(func)
    return wrapper


@test_time
def func1(n):
    return n


@test_time
def func2(n):
    return n


res1 = func1(3)
res2 = func2(3)

print(f'res_func1 = {res1}', f'res_func2 = {res2}', sep='\n')
