'''  Пример словаря, заполняемого в процессе эксплуатации.
Не сохраняется при выходе из программы  '''

words = {}
while True:
    s = input('Введите слово для перевода: ')
    if s == '':
        print('Выход из программы!!!', 'Содержимое вашего словаря:', sep='\n')
        print()
        for i, j in words.items():
            print(i, '=', j)
        break
    if s in words:
        print('Слово', s, 'переводится как', words)
    else:
        words[s] = input("Введите значение этого слова: ")
        if words[s] == '':
            del words[s]
            continue
        continue
with open('vocabulary_db.txt', 'a+') as vocabulary_db:
    vocabulary_db.writelines(str(words))
    vocabulary_db.writelines(", ")
    pass
'''Слова для копирования в словарь для проверки работы (чтобы не набирать вручную)'''
# dog = собака
# cat = котик
