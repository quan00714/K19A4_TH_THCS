a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

# a. Chuyển phần tử dương lên đầu
duong = [x for x in a if x > 0]
am_khong = [x for x in a if x <= 0]
a_new = duong + am_khong
print("Danh sách sau khi chuyển dương lên đầu:", a_new)

# b. Chèn số m
m = int(input("Nhập số m cần chèn: "))
# Đầu danh sách
a1 = [m] + a
print("Chèn vào đầu:", a1)
# Cuối danh sách
a2 = a + [m]
print("Chèn vào cuối:", a2)
# Vị trí thứ 5
a3 = a[:]
if len(a3) >= 5:
    a3.insert(4, m)
else:
    a3.append(m)
print("Chèn vào vị trí thứ 5:", a3)