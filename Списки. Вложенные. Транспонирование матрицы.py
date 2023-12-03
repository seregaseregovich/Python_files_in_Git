a = [[0, 10, 20, 30], [40, 50, 60, 70], [80, 90, 100, 110]]
for i in a:
    print(i)
print()
y = [[row[i] for row in a] for i in range(len(a[0]))]
for i in y:
    print(i)
    