import io
import token
import tokenize

# Создаем многострочную строку с кодом.
code_example = '''# Это словарь - именованная коллекция объектов.
my_dict = {'Имя': 'Python', 'Версия': "3.9.0"}

# Выводим значения на экран. 
print(my_dict['Имя'], my_dict['Версия'])'''

# Это позволит нам работать со строкой, как с файловым объектом.
rl = io.StringIO(code_example).readline
# Разбиваем код на токены, т.е. лексемы с указанием
# места их расположения в коде.
tkns = tokenize.generate_tokens(rl)
# Проходимся по всем токенам циклом.
for tkn in tkns:
    # Выводим тип, имя и саму лексему.
    print(tkn[0], ' -> ', token.tok_name[tkn[0]], ' -> ', tkn[1])
