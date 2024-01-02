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
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_nod2(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# get_nod = test_time(get_nod) - вместо этой строки
# ставим декоратор @test_time перед этой функцией
res = get_nod(2, 100000)


# get_nod2 = test_time(get_nod2) - вместо этой строки
# # ставим декоратор @test_time перед этой функцией
res2 = get_nod2(2, 100000)

print(res, res2, sep='\n')


# https://www.youtube.com/watch?v=v0qZPplzwUQ&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=47
