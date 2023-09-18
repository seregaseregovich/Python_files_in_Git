
# Программа для определения максимальной длины монотонного 
# фрагмента. Монотонный фрагмент - фрагмент, в котором 
# цифры либо постоянно возрастают, либо уменьшаются
#
#
d = "Y"
sps = []
sps1 = [0]
sps2 = [0]
while d == "Y" or d == "y":
    a1 = n1 = n2 = 0
    while d == "Y" or d == "y":
        while True:
            a = input("Enter the number : ")
            try:
                a = int(a)
            except ValueError:
                print("ОШИБКА! Это не целое число, попробуйте снова! ")
            else:
                break
        if a == 0:
                break
        print(a)
        while a > a1:
            n2 = 0
            n1 += 1
            a1 = a
            sps1.append(n1)
        while a < a1:
            n1 = 0
            n2 += 1
            a1 = a
            sps2.append(n2)
    if max(sps1) > max(sps2):
        print(max(sps1))
    if max(sps2) > max(sps1):
        print(max(sps2))
    if max(sps1) == max(sps2):
        print(max(sps1))
    d = input('if you want to continue, enter "Y". \nIf you want to finish, enter any key: ')
print("Dosvidos!!!")

