import re

'''ПРИМЕР получения данных из файла map.xml при помощи методов RE.

Дополнительный файл - map.xml'''


# ВАРИАНТ 1:
# ==========================================

with open("map.xml", "r") as f1:
    lat1 = []
    lon1 = []
    pattern1 = r"<point\s+[^>]*?lon=([\'\"])([0-9\.\,]+)\1\s+[^>]*lat=([\'\"])([0-9\.\,]+)\3"
    for txt1 in f1:
        match1 = re.findall(pattern1, txt1)
        if len(match1) > 0:
            lon1.append(match1[0][1])
            lat1.append(match1[0][3])
            print(match1)
    print(lon1, lat1, sep='\n')


# ВАРИАНТ 2:
# ==========================================

with (open("map.xml", "r") as f2):
    lat2 = []
    lon2 = []
    pattern2 = r"<point\s+[^>]*?lon=([\'\"])(?P<lon>[0-9\.\,]+)\1\s+[^>]*lat=([\'\"])(?P<lat>[0-9\.\,]+)\3"
    for txt2 in f2:
        match2 = re.search(pattern2, txt2)
        if match2:
            v = match2.groupdict()  # метод объекта сопоставления шаблона
            # со строкой match.groupdict() возвращает словарь, содержащий
            # все именованные подгруппы совпадения, помеченные
            # именем подгруппы name.
            # В нашем случае это (?:<lon>...) и (?P<lat>...) .
            print("v =", v)
            if "lon" in v and "lat" in v:
                lon2.append(v["lon"])
                lat2.append(v["lat"])
    print(lon2, lat2, sep='\n')
