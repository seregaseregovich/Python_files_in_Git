# ВАРИАНТ 1:
# ===============================================
# При помощи функции sorted() и лямбда-функции как ключ:

users = [
    {'name': 'Vasya', 'age': 55, 'salary': 100},
    {'name': 'Peter', 'age': 28, 'salary': 500},
    {'name': 'Peter', 'age': 27, 'salary': 200},
    {'name': 'Masha', 'age': 37, 'salary': 300},
    {'name': 'Allah', 'age': 24, 'salary': 200}
]

# Для сортировки по одному ключу:
lst = sorted(users, key=lambda x: x['salary'])
for i in lst:
    print(i)
print()

# Для сортировки по двум ключам
# внутри функции lambda используем скобки для
# создания кортежа с необходимыми ключами:
lst = sorted(users, key=lambda x: (x['name'], x['age']))
for i in lst:
    print(i)
print()


# ВАРИАНТ 2:
# ===============================================
# При помощи функции sorted() и функции как ключ:

def sortfunc(x):
    return x['salary']
    # для нескольких ключей:
    # return x['salary'], x['age']


users = [
    {'name': 'Vasya', 'age': 55, 'salary': 100},
    {'name': 'Peter', 'age': 28, 'salary': 500},
    {'name': 'Peter', 'age': 27, 'salary': 200},
    {'name': 'Masha', 'age': 37, 'salary': 300},
    {'name': 'Allah', 'age': 24, 'salary': 200}
]

lst = sorted(users, key=lambda x: sortfunc(x))
for i in lst:
    print(i)


# ВАРИАНТ 3:
# ================================================
# Сортировка обычного словаря:

d1 = {
    'river': "река",
    'house': "дом",
    'tree': "дерево",
    'road': "дорога"
}

d1 = dict(sorted(d1.items()))
print(d1)
# результат:
d1 = {
    'house': 'дом',
    'river': 'река',
    'road': 'дорога',
    'tree': 'дерево'
}
