# Петля.
# Работает до тех пор, пока не ввести
# три числовых значения через пробел

def take3Input():
    loop = True
    while loop:
        try:
            n, h, y = input("Enter three values: ").split(" ")
            loop = False
        except:
            print("please input 3 values")


take3Input()
