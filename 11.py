import operator
import Функция_Обратный_отсчет

dict1 = {
    'Sergei': {'date': 12, 'month': 'may', 'year': 1975, 'sex': 'male'},
    'Helen': {'date': 16, 'month': 'june', 'year': 1976, 'sex': 'female'}
}
for i in dict1:
    if dict1[i]['year'] > 1971:
        print(f'{i}, date of birth {dict1[i]['date']} {dict1[i]['month']} {dict1[i]['year']}')

sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(0), reverse=False)
print(dict1, dict(sorted_dict1), sep='\n')
x = int(input("Enter the integer number: "))
for i in Функция_Обратный_отсчет.countdown(x):
    print(i)
