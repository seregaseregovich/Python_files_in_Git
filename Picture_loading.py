''' Как скачать картинку с сайта на Python?

В этом примере мы используем функцию get()
из библиотеки requests для отправки GET-запроса
на указанный URL. Затем мы проверяем статусный
код ответа: если он равен 200, то картинка
успешно загружена, и мы записываем ее содержимое
в файл с расширением '.png'. Если же статусный код
не равен 200, то возникла ошибка при загрузке. '''

import requests

# https://docs.wxpython.org/_static/phoenix_main.png - URL адрес скачиваемой картинки

url = 'https://docs.wxpython.org/_static/phoenix_main.png'
response = requests.get(url)

if response.status_code == 200:
    with open('phoenix_main.png', 'wb') as file:
        file.write(response.content)
        print('Картинка сохранена!')
else:
    print('Ошибка при загрузке: ', response.status_code)
