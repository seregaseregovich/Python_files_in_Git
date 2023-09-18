#  Способ 1:

a = [[2, 3, 5], [1, 4, 2], [4, 1, 4], [2, 2, 3], [2, 5, 1]]
print(a)
a.sort(key=lambda x: x[2])
print(a)


#  Способ 2.1:

def last(n):
    return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


print(sort_list_last([(2, 5), (1, 2), (4, 4), (3, 3), (5, 1)]))


# Способ 2.2:

def sort_list(lst, func):
    return sorted(lst, key=func)


list1 = [1, 3], [-2, 9], [-5, 4], [2, 5]
print(sort_list(list1, lambda x: x[1]))


#  Способ 3

def average_result(x):  # Вычисление среднего арифметического результата
    #  данных по индексам [1], [2], [3] в каждой из строк s1, s2 s3
    y = (x[1] + x[2] + x[3]) / 3
    x.append(y)  # Добавление результата в конец списка
    return x


s1 = ['Ivanov', 3, 5, 7]
s2 = ['Petrov', 4, 8, 8]
s3 = ['Sidoroff', 2, 6, 9]
s = []
s.append(average_result(s1))
s.append(average_result(s2))
s.append(average_result(s3))
s.sort(key=lambda x: x[3], reverse=True)  # Сортировка списков s1-s3
# по индексу [3] в обратном порядке (reverse=True)
for i in s:
    print(i)
