''' 1. Необходимо подсчитать количество одинаковых элементов списка
и оформить результат в словарь. Необходимо отсортировать словарь
по ключу или по значению. '''

# Модуль collection необходим для подсчета количества одинаковых элементов в списке.
# Используем метод collections.Counter(my_list).
import collections
import operator

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# Для подсчета количества одинаковых элементов используем
# метод collections.Counter(my_list) из коллекции collections.
# Результат оформляем в виде словаря.
dict_res = dict(collections.Counter(my_list))
print(dict_res)
# Результат - {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# Для сортировки элементов словаря по ключу или значению используем
# метод sorted(dict.items(), key=operator.itemgetter(0), reverse=False)
# из коллекции operator, где:
# - operator.itemgetter(0), где 0 - сортировка по ключу, 1 - сортировка по значению;
# - reverse=False - по возрастанию, reverse=True - по убыванию.
sorted_dict_res = sorted(dict_res.items(), key=operator.itemgetter(0), reverse=False)
print(dict(sorted_dict_res))
# Результат - {10: 4, 20: 4, 30: 1, 40: 2, 50: 2}


'''2. Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key»
cо значением «new_value». Выведите на печать итоговый
словарь. Важно, чтобы словарь остался тем же (имел тот же
адрес в памяти).'''

from collections import OrderedDict

ddd = {3: '3', '2': '2', 33: '3', '4': '4', 5: '5'}
first = list(ddd.items())[0]
dct = OrderedDict(ddd)
print(ddd)
print(dict(dct))
dct.move_to_end('4', last=False)
print(dict(dct))
# задача требует проверки, возможны несоответствия


''''''