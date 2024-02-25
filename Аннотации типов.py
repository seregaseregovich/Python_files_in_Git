''' Аннотации типов.
Урок на YouTube:
https://www.youtube.com/watch?v=29WDYmT4e1E
'''


# ПРИМЕР 1:
# =======================================================.
# Использование аннотации типов данных (типичный пример):


def mult1(x: int, y: int = 4) -> str:
    return str(x * y)


print(mult1(2), mult1.__annotations__)
# 8 {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'str'>}


# ПРИМЕР 2:
# ================================================.
# Использование аннотации нескольких типов данных
# без применения сторонней импортируемой библиотеки
# (с использованием символа объединения "|"):


def mult2(x: int | float, y: int | float = 44) -> int | float | str:
    return str(x * y)


print(mult2(2), mult2.__annotations__)
# 88 {'x': int | float, 'y': int | float, 'return': int | float | str}


# ПРИМЕР 3:
# ================================================.
# Использование аннотации нескольких типов данных
# с применением сторонней импортируемой библиотеки:


from typing import Union, Optional, Any, Final


def mult3(x: Union[int, float], y: Union[int, float] = 444) -> Union[int, float, str]:
    return str(x * y)


print(mult3(2), mult3.__annotations__)
# 888 {'x': typing.Union[int, float], 'y': typing.Union[int, float],
# 'return': typing.Union[int, float, str]}
