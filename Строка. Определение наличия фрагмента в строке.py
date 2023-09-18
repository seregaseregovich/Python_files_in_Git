## Определяет, присутствует ли фрагмент "da"
## в строке "231da52yfgdadjh05513iudauh85521da"


from timeit import default_timer as timer
start = timer()


## ВАРИАНТ 1: Использование метода count
##------------

a = "231da52yfgdadjh05513iudauh85521da"
print(a.count("da"))

end = timer()
print("Control time taken:", end-start)


## ВАРИАНТ 2: Использование while
##------------

start = timer()
 
a = "231da52yfgdadjh05513iudauh85521da"
b = "da"
n = 0
while a.find(b) != -1:
    a = a[a.find(b) + len(b):]
    print(a)
    n += 1
print(n)

    
end = timer()
print("Control time taken:", end-start)


## ВАРИАНТ 3: Использование for
##------------

start = timer()

a = "231da52yfgdadjh05513iudauh85521da"
b = "da"
n = 0
for i in range(len(a) - 1):
    c = a[i] + a[i+1]
    if b == c:
        n += 1
print(n)

end = timer()
print("Control time taken:", end-start)

