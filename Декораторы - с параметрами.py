import math


def dx_dec(dx=0.0001):
    def func_dec(func):
        def wrapper(x, *ag, **kg):
            res = (func(x + dx, *ag, **kg) - func(x, *ag, **kg)) / dx
            return res

        return wrapper
    return func_dec


@dx_dec(dx=0.01)
def sin_df(x):
    return math.sin(x)


a = sin_df(math.pi / 3)
print(a)
