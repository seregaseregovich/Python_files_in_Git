n = int(input())
h = n//60
m = n % 60
if h > 23:
    h = h % 24
    print(h, ' hours', m, 'minutes')
else:
    print(h, ' hours', m, 'minutes')
