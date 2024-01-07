txt1 = ("Twinkle, twinkle, little star, "
        "How I wonder what you are! "
        "Up above the world so high, "
        "Like a diamond in the sky. "
        "Twinkle, twinkle, little star, "
        "How I wonder what you are! "
        "Up above the world so high, "
        "Like a diamond in the sky. "
        "Twinkle, twinkle, little star, "
        "How I wonder what you are! "
        "Up above the world so high, "
        "Like a diamond in the sky.")
print(txt1)
txt2 = txt1.split(' ')
print(txt2)
temp = []
txt3 = []
for i in txt2:
    if str(i).istitle() and len(i) > 1:
        txt3.append(temp)
        temp = []
        temp.append(i)
    else:
        temp.append(i)
txt3.append(temp)
del txt3[0]
n = 1
for i in txt3:
    if n == 1:
        print(' '.join(i))
        n += 1
    elif n == 2:
        print('\t', ' '.join(i))
        n += 1
    elif n == 3:
        print('\t', '\t', ' '.join(i))
        n += 1
    elif n == 4:
        print('\t', '\t', ' '.join(i))
        n = 1
