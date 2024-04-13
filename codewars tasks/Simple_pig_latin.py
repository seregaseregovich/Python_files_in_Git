""" Simple Pig Latin """

'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched..

Examples (input --> output):
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


# MY SOLUTION 1:
# =====================================================


def pig_it1(text):
    lst = []
    for i in text.split():
        if len(i) == 1:
            if i not in ('?', '!'):
                lst.append(i + 'ay')
                continue
            else:
                lst.append(i)
                continue
        else:
            lst.append(i[1:] + i[0] + 'ay')
    return ' '.join(lst)


print(pig_it1('j Pig latin is cool ?'))


# BEST SOLUTIONS:
# =====================================================
def pig_it2(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay'
                     if word.isalpha() else word for word in lst])


def pig_it3(text):
    return " ".join(x[1:] + x[0] + "ay"
                    if x.isalnum() else x for x in text.split())


import re


def pig_it4(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)


print(pig_it2('j Pig latin is cool ?'))
print(pig_it3('j Pig latin is cool ?'))
print(pig_it4('j Pig latin is cool ?'))
