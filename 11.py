import operator

dict1 = {
    'Sergei': {'date': 3, 'month': 'september', 'year': 1975},
    'Helen': {'date': 6, 'month': 'february', 'year': 1973}
}
for i in dict1:
    if dict1[i]['year'] > 1971:
        print(f'{i}, date of birth {dict1[i]['date']} {dict1[i]['month']} {dict1[i]['year']}')

sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(0), reverse=False)
print(sorted_dict1)
