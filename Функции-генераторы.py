''' Функции-генераторы. '''


# ВАРИАНТ 1 (простейший):
# ========================


def gen():
    for i in [1, 2, 3, 4]:
        yield i


# a = gen()
# for i in range(4):
#     print(next(a))

for i in gen():
    print(i)


# ВАРИАНТ 2:
# ========================

# Вычисление среднего арифметического последовательностей:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2, 3, 4, 5, 6, 7, 8, 9, 10
# 3, 4, 5, 6, 7, 8, 9, 10
# 4, 5, 6, 7, 8, 9, 10
# 5, 6, 7, 8, 9, 10
# 6, 7, 8, 9, 10
# 7, 8, 9, 10
# 8, 9, 10
# 9, 10


def gen():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a = gen()
print(list(a))


# [5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]


# ВАРИАНТ 3:
# ===================================
# Пример поиска индексов искомого
# фрагмента "фабий" в тексте файла.txt.

def gen(file, word):
    file_index = 0
    for line in file:
        line_index = 0
        while line_index != -1:
            line_index = line.find(word, line_index)
            if line_index != -1:
                yield line_index + file_index
                line_index += 1
        file_index += len(line)


try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        a = gen(file, 'фабий')
        print(list(a))
except FileNotFoundError:
    'File not found!'
except:
    print('No words was found!')
