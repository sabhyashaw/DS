import re

# 1
email = "example@test.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(pattern, email)))

# 2
txt = "Hello there Heooo"
x = re.findall(r"He.*o", txt)
print(x)

# 3
txt = "Ant bat fat cat flat brat"
x = re.findall(r"\b[aAfFbB]\w*t\b", txt, re.IGNORECASE)
print(x)

# 4
txt = "a123# aabc# a456# abc#"
x = re.findall(r"a.*?#", txt)
print(x)
print(len(x))
