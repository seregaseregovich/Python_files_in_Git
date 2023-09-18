# Вариант 1. Размерность матрицы вводится через пробел.
# Заполнение матрицы нулями

m, n = list(map(int, input('Введите M и N через пробел: ').split()))
print(m, n)
a = []
for i in range(m):
    a.append([0] * n)
print(a)

# Результат - [[0, 0, 0], [0, 0, 0]]


# Вариант 2: Заполнение - рандомное

import random

m = 4
n = 3
a = [[random.randint(1, 6) for i in range(m)] for j in range(n)]
print(a)
for i in a:
    print(i)

#  Модуль рандом можно заменить нулём или ещё чем-нибудь.

# ============================================================
# Как выбрать из содержимого матрицы ту или иную строку:

import random

m = 7
n = 7
# Создаем матрицу M x N с рандомным наполнением (цифрами от 1 до 6):
s = [[random.randint(1, 6) for i in range(m)] for j in range(n)]
for i in s:
    print(i)  # вывод на печать для наглядности

# Как выбрать из матрицы:
# -----------------------------

# 1. Всё содержимое ПОСТРОЧНО
# слева направо, сверху вниз:
a = [s[i][j] for i in range(m) for j in range(n)]
# выборка одной конкретной строки:
a1 = [s[3][i] for i in range(m)]

# 2. Всё содержимое ПО СТОЛБЦАМ
# сверху вниз, слева направо:
b = [s[j][i] for i in range(m) for j in range(n)]
# выборка одного конкретного столбца:
b1 = [s[i][3] for i in range(n)]

# 3. Содержимое ПО ДИАГОНАЛИ (для равносторонней матрицы):
# --- с левого верхнего угла:
c = [s[i][j] for i in range(m) for j in range(n) if i == j]
print(' ', c, sep='\n')
# --- с правого верхнего угла:
d = [s[i][(m-1)-i] for i in range(m)]
print(' ', d, sep='\n')
# --- с левого нижнего угла:
e = [s[i][(m-1)-i] for i in range(m-1, -1, -1)]
print(' ', e, sep='\n')
# --- с правого нижнего угла:
f = [s[i][j] for i in range(m, -1, -1) for j in range(n) if j == i]
print(' ', f, sep='\n')

# =======================================================
# Преобразование матрицы 4х4
# Перестановка содержимого столбцов
# из слева-направо в сверху-вниз

a = [[1, 2, 3, 4], [5, 6, 7, 8],
     [9, 10, 11, 12], [13, 14, 15, 16]]
for i in a:
    for j in i:
        print(j, end='\t')
    print()

for i in range(len(a)):
    for j in range(i+1, len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for i in a:
    for j in i:
        print(j, end='\t')
    print()

# Результат:

# 1	 2	3	4
# 5	 6	7	8
# 9	 10	11	12
# 13 14	15	16

# 1	 5	9	13
# 2	 6	10	14
# 3	 7	11	15
# 4	 8	12	16


# =======================================================

# ТАБЛИЦА УМНОЖЕНИЯ:

# Первый вариант:
m = 10
n = 10
s = [[f'{i} x {j} = {i*j}' for i in range(1, m)] for j in range(1, n)]
for i in s:
    print(i)

# Второй вариант:
n = [f'{i} x {j} = {i*j}' for i in range(1, 10) for j in range(1, 10)]
for i in range((10-1)**2):
    print(n[i])
