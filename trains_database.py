with open('trains_db.txt', 'a+'):
    print('File created')
    # trains_dict.write('{}, ')
    pass

trains_dict = dict()
trains_list = list()
yes = 'y'
y = ['y', 'Y', 'да', 'Да', 'ДА', 'yes', 'Yes', 'YES']
while yes in y:
    train_number = int(input('Input train number: '))
    trains_list.append(train_number)
    departure_point = input('Departure_point: ')
    departure_time = input('Departure_time (format xx:xx) : ')
    arrival_point = input('Arrival_point: ')
    arrival_time = input('Arrival_time (format xx:xx) : ')
    travel_time = input('Travel_time (format xx:xx) : ')

    trains_dict = {'departure_point': departure_point,
                   'departure_time': departure_time,
                   'arrival_point': arrival_point,
                   'arrival_time': arrival_time,
                   'travel_time': travel_time}
    trains_list.append(trains_dict)
    with open('trains_db.txt', 'a+') as trains_db:
        print('File created')
        trains_db.write(str(trains_list))
        trains_db.write(", ")
        pass
    print('train number', train_number, 'with the data:',
          trains_list[1], 'has been in database.')
    trains_list = list()
    yes = input('Will you continue to update the database? ')
    if yes in y:
        a1 = input('Will you continue to delete some data from the database? ')

print('Database has been updated.')
for i in trains_list:
    print('Train', i, ' has been added to the database.')
