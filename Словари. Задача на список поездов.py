# Создать список поездов. Структура словаря: номер поезда, пункт и время
# прибытия, пункт и время отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20 минут.
# Пример:
# list_of_trains = [
# {"number": "", "point_A": “", "start": "",
# "point_B": "", "end": ""},
#
#
# Я создал не список поездов, а словарь, внутри которого словари поездов
# .…


trains_dict = dict()
yes = 'y'
y = ['y', 'Y', 'да', 'Да', 'ДА', 'yes', 'Yes', 'YES']
while yes in y:
    train_number = int(input('Input train number: '))
    departure_point = input('Departure_point: ')
    departure_time = input('Departure_time (format xx:xx) : ')
    arrival_point = input('Arrival_point: ')
    arrival_time = input('Arrival_time (format xx:xx) : ')
    travel_time = input('Travel_time (format xx:xx) : ')

    trains_dict[train_number] = {'departure_point': departure_point,
                                 'departure_time': departure_time,
                                 'arrival_point': arrival_point,
                                 'arrival_time': arrival_time,
                                 'travel_time': travel_time}

    print('train number', train_number, 'with the data:', 
          list(trains_dict[train_number].items()), 'has been in database.')
    yes = input('Will you continue to update the database? ')
    if yes in y:
        a1 = input('Will you continue to delete some data from the database? ')
        print(a1)

print('Database has been updated.')
for i in trains_dict:
    print('Train number', i)
