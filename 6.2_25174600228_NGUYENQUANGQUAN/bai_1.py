# Nhập danh sách từ bàn phím
n = int(input("Nhập số phần tử của danh sách: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

# a. Tổng các phần tử
print("Tổng các phần tử:", sum(a))

# b. Đếm số lượng số dương và tổng số dương
duong = [x for x in a if x > 0]
print("Số lượng số dương:", len(duong))
print("Tổng các số dương:", sum(duong))

# c. Vị trí phần tử âm đầu tiên
vt_am = -1
for i in range(len(a)):
    if a[i] < 0:
        vt_am = i
        break
print("Vị trí phần tử âm đầu tiên:", vt_am if vt_am != -1 else "Không có")

# d. Vị trí phần tử dương cuối cùng
vt_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vt_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng:", vt_duong_cuoi if vt_duong_cuoi != -1 else "Không có")

# e. Phần tử lớn nhất và vị trí cuối cùng
max_val = max(a)
max_index = len(a) - 1 - a[::-1].index(max_val)
print("Phần tử lớn nhất:", max_val)
print("Vị trí phần tử lớn nhất cuối cùng:", max_index)