# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key»
# со значением «new_value». Выведите на печать итоговый
# словарь. Важно, чтобы словарь остался тем же (имел тот же
# адрес в памяти).

from collections import OrderedDict

ddd = {3: '3', '2': '2', 33: '3', '4': '4', 5: '5'}
first = list(ddd.items())[0]
dct = OrderedDict(ddd)
print(ddd)
print(dict(dct))
dct.move_to_end('4', last=False)
print(dict(dct))
