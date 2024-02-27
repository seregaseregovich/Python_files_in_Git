'''PERSISTENT BUGGER'''

"""Write a function, persistence, that takes in a positive 
parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits 
in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4,
and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 
and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)"""


# ВАРИАНТ 1 (МОЙ):
# ================================.

def persistence1(n):
    if len(str(n)) == 1:
        return 0
    count = 0
    while len(str(n)) > 1:
        count += 1
        c = 1
        print(n)
        for i in str(n):
            c *= int(i)
        n = c
    return count


print(persistence1(999))


# ВАРИАНТ 2.1:
# =================================================.

from functools import reduce


def persistence2(n, c=0):
    return persistence2(reduce(lambda x, y: int(x) * int(y), str(n)), c + 1) if n > 9 else c


# ВАРИАНТ 2.2:
# ==================================================.

persistence3 = lambda n, c=0: persistence3(reduce(lambda x, y: int(x)*int(y), str(n)), c+1) if n >= 10 else c


print(persistence2(45))
