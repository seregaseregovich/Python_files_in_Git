n = int(input())
h = n//60
m = n % 60
if h > 23:
    h = h % 24
    print(h, m)
else:
    print(h, m)
