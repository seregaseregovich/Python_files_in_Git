print('======================================', 'Вариант 1:', sep='\n')

d = {}
# s = 'abcdefghijklmnopqrstuvwxyz '
s = 'aaasssaa'  # Слово, в котором хотим подсчитать кол-во букв
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
        # if i in d:    можно использовать эту конструкцию вместо строки выше
        #     d[i] += 1
        # else:
        #     d[i] = 1
print(d, s, sep='\n')
for i in sorted(d):
    print(i, d[i])
print('======================================', 'Вариант 2:', sep='\n')

'''ВАРИАНТ 2:'''

d = {}
s = 'aaasssaa'  # Слово, в котором хотим подсчитать кол-во букв
letters = [0] * 26
for i in s.lower():
    if i.isalpha():
        d[i] = d.get(i, 0) + 1

print(d)
