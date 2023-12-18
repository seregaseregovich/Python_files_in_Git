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
# - ...itemgetter(0), где 0 - сортировка по ключу, 1 - сортировка по значению;
# - reverse=False - по возрастанию, reverse=True - по убыванию.
sorted_dict_res = sorted(dict_res.items(), key=operator.itemgetter(0), reverse=False)
print(dict(sorted_dict_res))
# Результат - {10: 4, 20: 4, 30: 1, 40: 2, 50: 2}
