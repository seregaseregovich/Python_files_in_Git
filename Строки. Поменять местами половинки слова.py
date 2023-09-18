s = input()
l = len(s)
lx = l//2 + l % 2
s1 = s[:lx]
s2 = s[lx:]
print(s2 + s1)

