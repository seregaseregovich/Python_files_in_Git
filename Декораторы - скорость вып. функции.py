import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Time = {dt} sec')
        return res

    return wrapper


@test_time
def to_binary1(n):
    for i in range(100000):
        continue
    return "{:0b}".format(n & 0xffffffff)


@test_time
def to_binary2(n):
    for i in range(100000):
        continue
    if n > 0:
        a = bin(int(n))
        return a[2:]
    elif n == 0:
        return '0'
    else:
        a = str(int(bin(2**32)[2:]) - int(bin(abs(n))[2:]))
        b = ''.join('1' if i == '9' else '0' for i in a)
        return b


# get_nod = test_time(get_nod) - вместо этой строки
# ставим декоратор @test_time перед этой функцией
res1 = to_binary1(3)


# get_nod2 = test_time(get_nod2) - вместо этой строки
# # ставим декоратор @test_time перед этой функцией
res2 = to_binary2(3)

print(res1, res2, sep='\n')


# https://www.youtube.com/watch?v=v0qZPplzwUQ&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=47
