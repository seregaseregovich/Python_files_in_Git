# Вариант 1:
# Декорирование.
# Сохранение имени декорируемой функции и её документации.
# ========================================================

import math


def dx_dec(dx=0.01):
    def func_dec(func):
        def wrapper(x, *ag, **kg):
            res = (func(x + dx, *ag, **kg) - func(x, *ag, **kg)) / dx
            return res

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return func_dec


@dx_dec(dx=0.00000001)
def sin_df(x):
    """Функция для вычисления синуса 1."""
    return math.sin(x)


print(sin_df.__name__, 'Вариант 1.')
print(sin_df.__doc__)

# Вариант 2:
# Декорирование.
# Сохранение имени декорируемой функции и её документации
# с помощью импортируемого модуля wraps
# =======================================================

from functools import wraps
import math


def dx_dec(dx=0.01):
    def func_dec(func):
        @wraps(func)
        def wrapper(x, *ag, **kg):
            res = (func(x + dx, *ag, **kg) - func(x, *ag, **kg)) / dx
            return res

        return wrapper

    return func_dec


@dx_dec(dx=0.00000001)
def sin_df(x):
    """Функция для вычисления синуса 2."""
    return math.sin(x)


print(sin_df.__name__, 'Вариант 2.')
print(sin_df.__doc__)
