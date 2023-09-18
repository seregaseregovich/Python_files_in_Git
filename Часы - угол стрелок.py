H = abs(int(input()))  # кол-во часов
M = abs(int(input()))  # кол-во минут
S = abs(int(input()))  # кол-во секунд
angle_1H = 360 / 12  # 30 град./ч
# angle_1M = 360 / 60 ## 6 гр./мин
# angle_1S = 360 / 60 ## 6 гр./сек
angle_1HM = 30 / 60  # Ч = 0,5 гр/мин
angle_1HS = 30 / 3600  # Ч = 0,0083333 гр/сек
angle_H = angle_1H * H + angle_1HM * M + angle_1HS * S
print(angle_H)
