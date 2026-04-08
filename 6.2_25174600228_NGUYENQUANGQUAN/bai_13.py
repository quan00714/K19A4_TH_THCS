import re
passwords = input("Nhập danh sách mật khẩu, cách nhau bởi dấu phẩy: ").split(",")
valid = []
for p in passwords:
    p = p.strip()
    if (6 <= len(p) <= 12 and
        re.search("[a-z]", p) and
        re.search("[A-Z]", p) and
        re.search("[0-9]", p) and
        re.search("[S#@]", p)):
        valid.append(p)
print(",".join(valid))