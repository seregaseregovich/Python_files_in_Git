from timeit import default_timer as timer
start = timer()

l = str(input("Enter the numbers, separating by the space: "))
l = [int(a) for a in (l.split(" "))]
print(l)
n = 0
s = 1
for x in l:
    for i in range(s, len(l)):
        if x == l[i]:
            n += 1
    s += 1
print(n)

end = timer()
print("Time taken:", end-start)
