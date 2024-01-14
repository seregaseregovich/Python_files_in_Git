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
