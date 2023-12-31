'''Data packing and unpacking:
*, **, args, kwargs'''


# An example of data packing:
# =====================================

a, *b, c = 'Hello'
print(a, b, c)  # res = H ['e', 'l', 'l'] o
a, b, *c = 1, 2, 3, 4, 5, 6, 7
print(a, b, c)  # res = 1 2 [3, 4, 5, 6, 7]
a, *_, c = 'Hello'
print(a, c)  # res = H o
a, b, *_ = 1, 2, 3, 4, 5, 6, 7
print(a, b)  # res = 1 2

# An example of data unpacking:
# =====================================

lst = [1, 2, 3, 4, 5]
a, *b = lst
print(a, b)  # res = 1 [2, 3, 4, 5]
*a, b = lst
print(a, b)  # res = [1, 2, 3, 4] 5
a, *b, c = lst
print(a, b, c)  # res = 1 [2, 3, 4] 5
a, *_, c = lst
print(a, c)  # res = 1 5
a, b, *_ = lst
print(a, b)  # res = 1 2

# Example of unpacking data from the list into the tuple:
# -------------------------------------------------------

a = [1, 2, 3]
b = (11, 12, 13) + (*a,)
print(b)  # res = (11, 12, 13, 1, 2, 3)

# Example of unpacking into the function RANGE:
# ---------------------------------------------
a = [1, 6]  # or tuple: a = (1, 6)
b = list(range(*a))
print(b)  # res = [1, 2, 3, 4, 5]
# The same example:
a = [1, 6]
b = [*(range(*a))]
print(b)  # res = [1, 2, 3, 4, 5]

# Example of data merging:
# ---------------------------------------------
a = [11, 12, 13, 14, 15]
b = 'abc'
c = [1, 4]
d = [*range(*c), *a, *b, *(True, False)]
print(d)  # res = [1, 2, 3, 11, 12, 13, 14, 15, 'a', 'b', 'c', True, False]

# Example of dictionary unpacking:
# ---------------------------------------------

dict1 = {
    1: 'one',
    2: 'two',
    3: 'three'
}
dict2 = {
    4: 'four',
    5: 'five',
    6: 'six'
}
a = {*dict1}
print(a)  # res = {1, 2, 3} - keys unpacked
a = {**dict1}
print(a)  # res = {1: 'one', 2: 'two', 3: 'three'} - dict. unpacked

# Unpacking and merging of two dictionaries:
# ---------------------------------------------
b = {**dict1, **dict2}
print(b)  # res = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}


# An example of using args and kwargs in the function:
# ====================================================


def os_path(disc, *args, sep='\\', **kwargs):
    args = (disc,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [i.strip() for i in args]
    path = sep.join(args)
    return path


p = os_path('f:', ' stepic.org ',
            ' Kind,_kind python ',
            '37\\39._Functions.docs', sep='/', trim=True)
print(p)
