try:
    print(sum([int(x) for x in input()]))
except ValueError:
    print('Failed')
