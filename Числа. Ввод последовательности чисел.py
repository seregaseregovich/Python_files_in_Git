d = "Y"
sps = []
while d == "Y" or d == "y":
    while True:
        a = input("Enter the number : ")
        try:
            a = int(a)
        except ValueError:
            print("ОШИБКА! Это не целое число, попробуйте снова! ")
        else:
            break
    print(a)
    if a != 0:
        sps.append(a)
    if a == 0:
        print("Amount of numbers: ", len(sps))
        sps = []
        d = input('if you want to continue, enter "Y". \nIf you want to finish, press any key: ')    
print("Dosvidos!!!")
