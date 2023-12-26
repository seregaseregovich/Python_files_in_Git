colour_name = ["Black", "Red", "Maroon", "Yellow"]
colour_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
res = [{'colour_name': a, 'colour_code': b} for a, b in zip(colour_name, colour_code)]
for i in res:
    print(i)
