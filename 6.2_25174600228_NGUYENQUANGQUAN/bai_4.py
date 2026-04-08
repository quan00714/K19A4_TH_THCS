a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

# a. Chèn [1,2,3] vào đầu, cuối, thứ 5
print("Đầu:", [1,2,3] + a)
print("Cuối:", a + [1,2,3])
if len(a) >= 5:
    a5 = a[:4] + [1,2,3] + a[4:]
else:
    a5 = a + [1,2,3]
print("Vị trí thứ 5:", a5)

# b. Xóa phần tử thứ k
k = int(input("Nhập vị trí k cần xóa: "))
if 0 <= k < len(a):
    a_del = a[:k] + a[k+1:]
    print("Sau khi xóa:", a_del)
else:
    print("Vị trí không hợp lệ")

# c. Sắp xếp tăng dần, giảm dần
a_tang = sorted(a)
a_giam = sorted(a, reverse=True)
print("Tăng dần:", a_tang)
print("Giảm dần:", a_giam)