# Пример 1:
# =================

import pickle

books = [
    ('Евгений Онегин', 'Пушкин А.С.', 200),
    ('МуМу', 'Тургенев И.С.', 250),
    ('Мастер и Маргарита', 'Булгаков М.А.', 500),
    ('Мертвые души', 'Гоголь Н.В.', 190)
]
try:
    with open('abc.bin', 'wb') as file:
        pickle.dump(books, file)
except:
    print('Mistake has been maked!')

try:
    with open('abc.bin', 'rb') as file:
        print(pickle.load(file))
except:
    print('Mistake has been maked!')


# Пример 2:
# =================
book1 = ['Евгений Онегин', 'Пушкин А.С.', 200]
book2 = ['МуМу', 'Тургенев И.С.', 250]
book3 = ['Мастер и Маргарита', 'Булгаков М.А.', 500]
book4 = ['Мертвые души', 'Гоголь Н.В.', 190]

try:
    with open('abc.bin', 'wb') as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except:
    print('Mistake has been made!')

try:
    with open('abc.bin', 'rb') as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)

        print(b1, b2, b3, b4, sep='\n')
except:
    print('Mistake has been maked!')

# RESULT:
# ['Евгений Онегин', 'Пушкин А.С.', 200]
# ['МуМу', 'Тургенев И.С.', 250]
# ['Мастер и Маргарита', 'Булгаков М.А.', 500]
# ['Мертвые души', 'Гоголь Н.В.', 190]
# Выводит построчно (также, как записывалось выше).
