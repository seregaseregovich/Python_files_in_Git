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

match1 = re.findall(r"<script.*?>([\w\W]+)(?=</script>)", txt1, re.MULTILINE)
print(match1)
