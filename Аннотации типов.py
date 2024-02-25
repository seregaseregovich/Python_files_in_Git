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


def mult2_1(x: int | float, y: int | float = 44) -> int | float | str:
    return str(x * y)


# ... или можно назначить типам данных свою переменную:
type_1 = int | float
type_2 = int | float | str


def mult2_2(x: type_1, y: type_1 = 44) -> type_2:
    return str(x * y)


print(mult2_1(2), mult2_1.__annotations__)
# 88 {'x': int | float, 'y': int | float, 'return': int | float | str}


# ПРИМЕР 3:
# ================================================.
# Использование аннотации нескольких типов данных
# с применением сторонней импортируемой библиотеки:


from typing import Union, Optional, Any, Final


def mult3_1(x: Union[int, float], y: Union[int, float] = 444) -> Union[int, float, str]:
    return str(x * y)


# ... или можно назначить типам данных свою переменную:
type_1 = Union[int, float]
type_2 = Union[int, float, str]


def mult3_2(x: type_1, y: type_1 = 44) -> type_2:
    return str(x * y)


print(mult3_1(2), mult3_1.__annotations__)
# 888 {'x': typing.Union[int, float], 'y': typing.Union[int, float],
# 'return': typing.Union[int, float, str]}
