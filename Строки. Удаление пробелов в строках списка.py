ll = [' - Скажи-ка,  дядя,    ведь  не    даром',
      'Москва,      спаленная  пожаром, ',
      'Французу   отдана?',
      'Ведь      были   ж схватки  боевые,',
      'Да, говорят,    еще какие!',
      'Недаром помнит вся    Россия',
      'Про      день Бородина!',
      ]

for i, line in enumerate(ll):
    while line.count('  '):
        line = line.replace('  ', ' ')
    ll[i] = line
print(ll)
