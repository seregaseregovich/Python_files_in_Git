# Программа для преобразования первых пяти и последних пяти
# элементов списка (возведение в степень)

n = 30 # определяем длину списка - 30
l1 = list(range(1, n + 1))
print(l1)
l21 = [a**2 for (i, a) in enumerate(l1) if i < 5]
print(l21)
l22 = [a for (i, a) in enumerate(l1) if (i >= 5) and i < (len(l1) - 5)]
print(l22)
l23 = [a**2 for (i, a) in enumerate(l1) if i >= (len(l1) - 5)]
print(l23)
l = l21 + l22 + l23
print(l)


# Либо вариант ниже с использованием функцииЖ


def ff(nn):
    l1 = list(range(1, nn + 1))
    print(l1)
    l21 = [a**2 for (i, a) in enumerate(l1) if i < 5]
    print(l21)
    l22 = [a for (i, a) in enumerate(l1) if (i >= 5) and i < (len(l1) - 5)]
    print(l22)
    l23 = [a**2 for (i, a) in enumerate(l1) if i >= (len(l1) - 5)]
    print(l23)

    return list(l21 + l22 + l23)


nn = 20
ll = ff(nn)
print(ll)