import re
pwd = input("Nhập mật khẩu: ")
if (6 <= len(pwd) <= 12 and
    re.search("[a-z]", pwd) and
    re.search("[A-Z]", pwd) and
    re.search("[0-9]", pwd) and
    re.search("[S#@]", pwd)):
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")