s = "Its now the time to collect the hurvest in the country"
l1 = len(s)
x = s[:2]
print(s)
for i in range(2, l1, 3):
    x = x + s[i + 1:i + 3]
print(x)
