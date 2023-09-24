# age = input("Введите ваш возраст, лет: ")
height = input("Введите ваш рост в см: ")
if type(height) == str:
    print("Введены каличные данные, начните сначала!")
height = int(height)
# weight = input("Введите ваш вес, кг: ")
H = [145, 148, 150, 153, 156, 158, 161, 164, 166, 168, 171, 173, 176, 178, 181, 184]
LW = []
MW = []
HW = []
# for lw in range (41, 68):
#    LW.append(lw)
# for mw in range (43, 73):
#    MW.append(mw)
# for hw in range(47, 79):
#    HW.append(hw)
if height <= H[12] and height >= H[11]:
    print("У вас нормальное телосложение")
elif height > H[11]:
    print("Ты слишком высокая! Стань на колени, и измерь свой рост заново!")
elif height < H[12]:
    print("Твой рост оказался слишком маленьким. Кушай побольше!")
else:
    print("Введены каличные данные, начните сначала!")
    print('beliberdy')
