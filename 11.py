dict1 = {
    'Sergei': {'date': 3, 'month': 'september', 'year': 1971},
    'Helen': {'date': 6, 'month': 'february', 'year': 1973}
}
for i in dict1:
    if dict1[i]['year'] > 1971:
        print(f'{i}, date of birth {dict1[i]['date']} {dict1[i]['month']} {dict1[i]['year']}')

