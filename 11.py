dict1 = {
    'на кол': 1,
    'неудовлетворительно': '2',
    'удовлетворительно': '3',
    'хорошо': '4',
    'отлично': '5',
}
dict2 = {key.upper(): int(value) for key, value in dict1.items()}
print(dict2)
