a = [[1, 2, 3, 4], [11, 22, 33, 44], [111, 222, 333, 444]]
b = [[10, 20, 30, 40], [100, 200, 300, 400], [1000, 2000, 3000, 4000]]
c = []
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)

print(c)
