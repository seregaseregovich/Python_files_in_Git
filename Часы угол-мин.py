a = abs(float(input()))
sa = (43200 * a) / 360
h = sa // 3600 % 12
h1 = sa // 3600
m = (sa - h1 * 3600) // 60
s = (sa - h1 * 3600 - m * 60) % 60
print(int(h), int(m), int(s))
