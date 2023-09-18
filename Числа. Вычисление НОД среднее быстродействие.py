# Вычисление наибольшего общего делитьеля (НОД)
# способом со средним быстродействием
m = int(input("Number-1: "))
n = int(input("Number-2: "))
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print(m)


# Примерно то же самое, оформленное в виде функцииЖ

def get_nod(a, b):
    '''Вычисление НОД для натуральных чисел а и b
    по алгоритму Евклида

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    '''
    while a != b:
        if a < b:
            a, b = b, a
        a = a - b
    return a


print(get_nod(18, 27))
help(get_nod)
