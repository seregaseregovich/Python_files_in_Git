import re

txt0 = "подоходный налог, доход, доходяга tthvjbhknj"
match0 = re.findall(r".+(?=яга)", txt0)
print(match0)

txt1 = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="vievport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

match1 = re.findall(r"""<script.*?>         # выделяем атрибут 1
                            ([\w\W]+)               # выделяем атрибут 1
                            (?=</script>)           # выделяем атрибут 1
                            """, txt1, re.MULTILINE | re.VERBOSE)
print(match1)

# https://www.youtube.com/watch?v=xYm6o-TrFeg&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=14
