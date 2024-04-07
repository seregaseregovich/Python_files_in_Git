'''Convert Integer to Binary (codewars).

Convert integer to binary as simple as that.
You would be given an integer as a argument
and you have to return its binary form.

Notes: negative numbers should be handled
as two's complement; assume all numbers are
integers stored using 4 bytes (or 32 bits)
in any language.

Your output should ignore leading 0s.

Examples (input --> output):
3  --> "11"
-3 -->"11111111111111111111111111111101"'''

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
    return "{:0b}".format(n & 0xffffffff)


@test_time
def to_binary2(n):
    if n > 0:
        a = bin(int(n))
        return a[2:]
    elif n == 0:
        return '0'
    else:
        a = str(int(bin(2 ** 32)[2:]) - int(bin(abs(n))[2:]))
        b = ''.join('1' if i == '9' else '0' for i in a)
        return b


res1 = to_binary1(3)
res2 = to_binary2(3)

print(res1, res2, sep='\n')

# Tests

# import codewars_test as test
# from solution import to_binary
#
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(to_binary(2),"10")
#         test.assert_equals(to_binary(3),"11")
#         test.assert_equals(to_binary(4),"100")
#         test.assert_equals(to_binary(5),"101")
#         test.assert_equals(to_binary(7),"111")
#         test.assert_equals(to_binary(10),"1010")
#         test.assert_equals(to_binary(-3),"11111111111111111111111111111101")
#         test.assert_equals(to_binary(0),"0")
#         test.assert_equals(to_binary(1000),"1111101000")
#         test.assert_equals(to_binary(-15),"11111111111111111111111111110001")
#         test.assert_equals(to_binary(-1000),"11111111111111111111110000011000")
#         test.assert_equals(to_binary(-999999),"11111111111100001011110111000001")
#         test.assert_equals(to_binary(999999),"11110100001000111111")
