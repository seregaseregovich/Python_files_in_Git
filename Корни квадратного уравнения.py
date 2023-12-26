## Квадратное уравнение имеет вид ax2 + bx + c = 0
## При его решении сначала вычисляют дискриминант по формуле
## D = b2 - 4ac, где Д - дискриминант.
## Если D > 0, то квадратное уравнение имеет два корня;
## если D = 0, то 1 корень; и если D < 0, то делают вывод, что корней нет.
## Если 2 корня:  x1 = (-b + math.sqrt(discr)) / (2 * a)
##                x2 = (-b - math.sqrt(discr)) / (2 * a)
## Если 1 корень: x = -b / (2 * a)

import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")