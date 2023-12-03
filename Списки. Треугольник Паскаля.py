n = 7
z = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(len(row)):
        if 0 < j < len(row) - 1:
            row[j] = z[i-1][j-1] + z[i-1][j]
    z.append(row)

for i in z:
    print(i)
