l1 = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
l2 = [x for row in l1 for x in row]
print(l1, l2, sep='\n')
l3 = l2[::-1]
print(l3 == l2[::-1])
