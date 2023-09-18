c = -1
a = 0
for i in range(1, 20, 2):
    c = c * (-1)
    a = a + (4 / i) * c
    print(a)
