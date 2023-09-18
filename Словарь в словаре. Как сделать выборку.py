a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 1997, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 2001, 'hobby': 'tennis', 'car': 'Smart'},
    'Gorbachev': {'age': 2000, 'hobby': 'soccer', 'car': 'Audi'},
    'Kostin': {'age': 2014, 'hobby': 'chess', 'car': 'Tata'},
    'Isaev': {'age': 1990, 'hobby': 'swimming', 'car': 'Mahindra'},
    'Eliseev': {'age': 1995, 'hobby': 'music', 'car': 'Lada Vesta'},
    'Kozlov': {'age': 2000, 'hobby': 'reading', 'car': 'UAZ'},
    'Bukov': {'age': 2002, 'hobby': 'theft', 'car': 'KAMAZ'},

}


b = [(elem, a[elem]['hobby'], a[elem]['car']) for elem in a if 1990 <= a[elem]['age'] < 2001]
for i in b:
    print(i[0], i[1])
print(b)
