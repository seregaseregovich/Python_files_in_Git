b = [1, 2, 3, 4, 5]
obj = range(len(b))
print(obj)
for i in obj:
    print(obj[i], "-", b[i])
k = list(enumerate(b, 3))
print(k)
# Функция enumerate(list, n) позволяет преобразовать последовательность list
# в набор кортежей, первым элементом каждого будет индекс n,
# вторым - элемент последовательности list.
# Если n не указать, то индекс по умолчанию начинается с нуля.
# Если задать значение n, то индекс начнется с этого числа.
