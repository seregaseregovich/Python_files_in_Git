"""Конструкция match-case, заменяющая if-elif-else.
   Достоинства и недостатки
   Ссылка - https://www.youtube.com/watch?v=torBLwByso0 """

# ПРИМЕР 1:
# =========

import timeit


def condition():  # Вариант 1
    response = 500
    if response == 200:
        return "Ok"
    elif response == 300:
        return "Redirect"
    else:
        return "Error"


def switch():  # Вариант 2
    response = 500
    match response:
        case 200:
            return "Ok"
        case 300:
            return "Redirect"
        case _:
            return "Error"


execution_time_1 = timeit.timeit(condition, number=100000)
print(f'Время выполнения {execution_time_1} секунд')

execution_time_2 = timeit.timeit(switch, number=100000)
print(f'Время выполнения {execution_time_2} секунд')
print()


# ПРИМЕР 2:
# ===========
#
#
# def condition():  # Вариант 1
#     response = 300
#     if response in [200, 201, 202, 203]:
#         return "Ok"
#     elif response in [300, 301, 302, 303]:
#         return "Redirect"
#     else:
#         return "Error"
#
#
# def switch():  # Вариант 2
#     response = 200
#     match response:
#         case 200 | 201 | 202 | 203:
#             return "Ok"
#         case 300 | 301 | 302 | 303:
#             return "Redirect"
#         case _:
#             return "Error"
#
#
# print(condition())
# print(switch())


# ПРИМЕР 3 (деструктуризация данных):
# ===================================
#
# point1 = [2, 5]
#
#
# def condition():  # Вариант 1
#     x, y = point1
#     if x == 0 and y == 5:
#         return "No move"
#     elif y == 5:
#         return f'Horisontal moving to point {x}'
#     elif x == 0:
#         return f'Horisontal moving to point {y}'
#     else:
#         return f'Moving to point x={x}, y={y}'
#
#
# points2 = [[3, 8], [2, 5], [2, 8]]
#
#
# def switch():      # Вариант 2
#     match points2[0]:
#         case 2, 5:
#             return 'No move'
#         case x, 5:
#             return f'Horisontal moving to point {x}'
#         case 2, y:
#             return f'Horisontal moving to point {y}'
#         case x, y:
#             return f'Moving to the point x={x}, y={y}'
#
#
# print(condition())
# print(switch())


# ПРИМЕР 4, с классами:
# ======================
#
#
# class Rectangle:
#     def __init__(self, wight, height):
#         self.wight = wight
#         self.height = height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#
# def calculate_area(shape):  # Вариант 1
#     if isinstance(shape, Rectangle):
#         print("Rectangle")
#         return shape.wight * shape.height
#     elif isinstance(shape, Circle):
#         print("Circle")
#         return 3.14159 * shape.radius * shape.radius
#     else:
#         return "Unknown shape"
#
#
# def calculate_area(shape):  # Вариант 2
#     match shape:
#         case Rectangle(wight=w, height=h):
#             print("Rectangle")
#             return h * w
#         case Circle(radius=r):
#             print("Circle")
#             return 3.14159 * r * r
#         case _:
#             return "Unknown shape"
#
#
# shape = Rectangle(3, 5)
# print(calculate_area(shape))
#
# shape = Circle(4)
# print(calculate_area(shape))


# ПРИМЕР 5:
# =========
#
#
# data0 = ['none']
# data1 = ['bot']
# data2 = ['user2']
# data3 = ['user3', 'bot', 25]
# data4 = ['user4', 'bot', 45, 2344, 'untitled']
#
#
# def age(data):  # Вариант 1
#     if isinstance(data, list) and len(data) > 2 and data[2] <= 60:
#         return print(f'Доступ к DATABASE {data[0]} разрешен')
#     else:
#         print(f'Доступ к DATABASE {data[0]} ЗАПРЕЩЕН!')
#
#
# def age(data):
#     match data:
#         case [_, _, age] if age <= 60:
#             print(f'Доступ к DATABASE {data[0]} разрешен')
#         case [_, _, age, *_] if age <= 60:
#             print(f'Доступ к DATABASE {data[0]} разрешен')
#         case _:
#             print(f'Доступ к DATABASE {data[0]} ЗАПРЕЩЕН!')
#
#
# age(data0)
# age(data1)
# age(data2)
# age(data3)
# age(data4)
