'''HUMAN READABLE TIME'''

'''Write a function, which takes a non-negative integer (seconds) 
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.'''


# My solution:
# ======================================

def make_readable(seconds):
    s = seconds % 60
    m = (seconds // 60) % 60
    h = seconds // 3600
    return f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}'


print(make_readable(60))


# One of the best solutions:
# =====================================


def make_readable(seconds):
    s = seconds % 60
    m = (seconds // 60) % 60
    h = seconds // 3600
    return '{:02}:{:02}:{:02}'.format(h, m, s)


print(make_readable(60))
