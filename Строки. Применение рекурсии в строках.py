#  Преобразовывает обычную строку в строку со скобками
#  между буквами. Скобки расположены внутрь друг-к-другу
#  по отношению к центру текста


#  ПРИМЕР 1

def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]


s = input()
print(rec(s))


#  ПРИМЕР 2

#  Добавляет зеркальную строку, в которой скобки будут
#  расположены наоборот

#  ВАРИАНТ 1

def rec(x):
    if len(x) == 1:
        if x != '(':
            return x + x
        return '()'
    if x[0] != '(':
        return x[0] + rec(x[1:]) + x[0]
    return '(' + rec(x[1:]) + ')'


x = input(str())
print(rec(x))

#   ВАРИАНТ 2

ss = ''
for i in range(1, len(s) + 1):
    if s[-i] == '(':
        ss = ss + ')'
    else:
        ss = ss + s[-i]
print(s + ss)

#  from timeit import default_timer as timer
#  start = timer()


#  end = timer()
#  print("Control time taken:", end-start)
