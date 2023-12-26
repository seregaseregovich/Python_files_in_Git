# СЛОВАТЬ dict
# Создаем пустой словарь
my_dict = {}
my_dict["country"] = "Mexico"  # Присваиваем ключу country значение Mexico
print(my_dict["country"])  # Выведет значение Mexico


# Заполнение словаря при инициализации
another_dict = {"number": 23, 2: True, "my_list": [1, 2, 3], 55: "myyyy"}
print(another_dict)
print(another_dict.keys())  # Напечатает список всех ключей
print(another_dict.values())  # Напечатает список всех значений


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
# a == b == c == d == e == f
print(a)
