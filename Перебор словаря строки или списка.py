s = [24, 24, "15164d", 695, "gr", "rjr", "r ftyh", 6547]
# или s = "gel;igm6556rts  lsb k s ksj 68465t fg bgf" (Строка)
for x in s:
    print(x, end="___")  # 24 24 15164d 695 gr rjr r ftyh 6547 Finish
else:
    print("Finish")

# То же самое для кортежей:
arr = [(1, 2), (3, 4)]  # Список из кортежей
for a, b in arr:
    print(a, b)
# 1 2
# 3 4

# То же самое для словаря:
arr = {
    "x": 1,
    "y": 2,
    "z": 33}
print(list(iter(arr.keys())), list(iter(arr.values())))
print(arr, '========')  # {'x': 1, 'y': 2, 'z': 33}
for key, values in arr.items():
    print(key, arr[key], values)
# x 1
# y 2
# z 33
for key in arr:
    print(key, arr[key])
# x 1
# y 2
# z 33
