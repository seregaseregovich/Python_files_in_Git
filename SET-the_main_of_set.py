# СЕТ set
# Создание пустого сета
s = set()
print(s)
# Создание сета инициализацией
s = {"hi", "bye"}
print(s)
# Для добавление элемента в сет используется add
# для удаления - pop (не разобрался как работает) или remove.
a = s
a.add(1)  #
a.add(2)  #
print(a)
a.add("str")  # можно добавлять только один аргумент в одной команде
print(a)
b = {2, 3}
print(b)
a.remove("str")
b.remove(2)
print(a, b)