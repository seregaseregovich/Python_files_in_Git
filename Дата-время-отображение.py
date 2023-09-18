import datetime
today = datetime.datetime.today()
print(f"{today:%d %b %Y, %A}")

# где:
#   A - день недели (sunday)
#   a - день недели сокращенно (sun)
#   B - месяц прописью (September)
#   b, h - месяц прописью сокращенно (sep)
#   D - дата (09/17/23)
#   d - день - число (17)
#   F - дата (2023-09-17)
#   H, I - ??? цифрами (09)
#   M - минуты (03)
#   m - месяц цифрами (09)
#   p - AM/PM
#   R - время (09:06)
#   r - время АМ (09:05:14 AM)
#   S - секунды (54)
#   T - время (09:08:07)
#   X - время (09:11:51)
#   x - дата (09/17/23)
#   Y - год полностью (2023)
#   y - год сокращенно (23)


print(f"{today:%c}")


# Еще пример с F строками:
# ========================


import datetime
name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
print(f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.')
# 'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
print(f'He said his name is {name!r}.')
# "He said his name is 'Fred'."
