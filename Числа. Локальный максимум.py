'''Определение количества локальных максимумов в последовательности'''
## чисел. 
## Локальный максимум - число, которое больше каждого из 
## соседних чисел в списке
##
## СТАРАЯ ПРОГРАММА ДЛЯ ПОИСКА ЛОКАЛЬНЫХ МАКСИМУМОВ
##
# d = "Y"
# sps = []
# n = 0
# while d == "Y" or d == "y":
#     while d == "Y" or d == "y":
#         while True:
#             a = input("Enter the number : ")
#             try:
#                 a = int(a)
#             except ValueError:
#                 print("ОШИБКА! Это не целое число, попробуйте снова! ")
#             else:
#                 break
#         if a == 0:
#                 break
#         print(a)
#         sps.append(a)
#         print(sps)
#     for i in range(len(sps) - 2):
#         if sps[i+1] > sps[i] and sps[i+1] > sps[i+2]:
#             print("Local maximum - ", sps[i + 1]) # вывод на печать локальных максимумов
#             n += 1
#     print("Amount of local maximum numbers: ", n)
#     d = input('if you want to continue, enter "Y". \nIf you want to finish, enter any key: ')
# print("Dosvidos!!!")

'''Отработанная программа для поиска локальных максимумов'''
l0 = [8, 6, 5, 4, 98, 6, 5, 3, 4, 98, 6, 5, 4, 6, 3, 1, 2, 2, 1, 8, 9, 0]
l1 = []
a = 0
for i in range(len(l0) - 1):
    if len(l0) > 2:
        if l0[0] >= l0[1] and len(l1) == 0:
            l1.append(l0[0])
            a = l0.pop(0)
        elif l0[0] >= l0[1] and l0[0] >= a:
            l1.append(l0[0])
            a = l0.pop(0)
        else:
            a = l0.pop(0)
    else:
        if l0[1] > l0[0]:
            l1.append(l0[1])
        elif l0[1] == l0[0]:
            l1.append(l0[0])
            l1.append(l0[1])
        else:
            l1.append(l0[0])
print(l1)
print(max(l1))

#  Удаление первого по вел-не локального максимума (чтобы определить второй):
l2 = l1[:]
for i in range(l2.count(max(l2))):
    l2.remove(max(l2))
print(l2)
print(max(l2))

#  Определение индекса последнего локального максимума

