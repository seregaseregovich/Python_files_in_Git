""" RGB TO HEX CONVERSION """

'''The rgb function is incomplete. Complete it so that passing 
in RGB decimal values will result in a hexadecimal representation 
being returned. Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the 
closest valid value.
Note: Your answer should always be 6 characters long, 
the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"'''


# MY SOLUTION 1:
# =====================================================


def rgb1(r, g, b):
    if r < 0:
        r = 0
    if r > 255:
        r = 255
    if g < 0:
        g = 0
    if g > 255:
        g = 255
    if b < 0:
        b = 0
    if b > 255:
        b = 255
    return (hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)).upper()


print(rgb1(-20, 275, 125))

# MY SOLUTION 2 (improved):
# ====================================================
# if x > 255, it is divided by 255 and then using a remainder of division.
# Example:
# 257 is rounded to 2 (257 % 255 = 2)
# 515 is rounded to 5 (515 % 255 = 5).


def rnd(x):
    if x <= 0:
        return 0
    return x % 255 if x > 255 else x


def rgb(r, g, b):
    return ("{:02X}" * 3).format(rnd(r), rnd(g), rnd(b))


print(rgb(-20, 275, 125))


# THE BEST SOLUTION:
# =====================================================


def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb2(-20, 275, 125))
