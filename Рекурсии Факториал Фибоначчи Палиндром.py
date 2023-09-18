from timeit import default_timer as timer

start = timer()

end = timer()
print("Control time taken:", end - start)

# =============================================

#    ФАКТОРИАЛ числа 4. СПОСОБ 1

a = 1
for i in range(1, 4):
    a = a * i
print(a)


#    ФАКТОРИАЛ числа 4. СПОСОБ 2

def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


print(fact(4))


# ==============================================

#   ЧИСЛО ФИБОНАЧИ.   СПОСОБ 1
#                  Пример ниже - для числа 6:
#                  0+1=1+2=3+2=5+3=8+5=13+8=21+13=34....
#                  - -   -   -   -    -    -
# сумма последовательно возрастающих двух чисел
# с полученным результатом.
# 1024 - максимально вычисляемое число в Python

def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return x + fib(x - 1)


print(fib(6))

#  Еще один вариант:

def fib(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)

#   ЧИСЛО ФИБОНАЧИ.   СПОСОБ 2
#   Пример ниже - для числа 6:
# Максимально вычисляемое число ограничено
# быстродействием (долго считает)
start = timer()
s = 0
for i in range(6 + 1):
    s += i
print(s)
end = timer()
print("Control time taken:", end - start)

#  Еще один вариантЖ
def fibo(x):
    if x == 0:
        return 0
    if x <= 2:
        return 1
    prev = 0
    cur = 1
    while x > 1:
        nex = cur + prev
        prev = cur
        cur = nex
        x -= 1
    return cur

#  ЧИСЛО ФИБОНАЧИ. СПОСОБ 3

def fib(n):
    a, b = 0, 1
    if n == 0: return 0
    for i in range(1, n):
        a, b = b, a + b
    return b

print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(10))


# ==============================================

#   ПАЛЛИНДРОМ (симметричное слово)


def pallindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return pallindrom(s[1:-1])


print(pallindrom('s2dsffsd2s'))

# ====================================
#  Палиндром - с помощью обысной функции:

def pallindrom(sequence):
    return list(sequence) + list(reversed(sequence))


l = 'abcdefgh'
print(''.join(pallindrom(l)))


# То же самое - с применением упаковки/распаковки (*):

def pallindrom(sequence):
    return [*sequence, *reversed(sequence)]


l = 'abcdefgh'
print(''.join(pallindrom(l)))


# Вычисление числа X в степени N:
def rec(x, n):
    if n == 0:
        return 1
    else:
        return x * rec(x, n-1)
