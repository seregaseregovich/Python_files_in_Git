""" Moving Zeros To The End """

'''Write an algorithm that takes an array and 
moves all of the zeros to the end, preserving 
the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) 
    returns [1, 1, 2, 1, 3, 0, 0]     '''


# MY SOLUTION:
# =====================================================


def move_zeros(lst):
    lst2 = [i for i in lst if i != 0]
    return lst2 + [0] * (len(lst) - len(lst2))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


# THE BEST SOLUTION:
# =====================================================


def move_zeros(lst):
    lst.sort(key=lambda v: v == 0)
    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
