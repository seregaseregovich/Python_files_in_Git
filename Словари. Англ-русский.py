# На входе - слово на английском, через тире - несколько его
# значений на русском, которые разделены запятой.
# Необходимо создать словарь, в котором ключ - слово на английском,
# а его значения - список из этих слов на русском

l1 = 'apple - яблоко'
l2 = 'orange - оранжевый, рыжий, апельсин'
l3 = 'grape - виноград, виноградный, гроздь'
l4 = 'easy - простой, легкий, нетрудный, удобный, несложный'
ll1 = (l1.replace(' ', '')).split('-')
ll2 = (l2.replace(' ', '')).split('-')
ll3 = (l3.replace(' ', '')).split('-')
ll4 = (l4.replace(' ', '')).split('-')
ll = [ll1, ll2, ll3, ll4]
print(ll)
d = {}
for i in ll:
    d[i[0]] = i[1].split(',')
print(d)
