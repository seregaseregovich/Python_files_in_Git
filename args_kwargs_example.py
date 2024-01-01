import time

start = time.time()


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

stop = time.time()
dt = stop - start
print(dt)
