m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Nhập A[{i}][{j}]: ")))
    A.append(row)

# Tính tổng
tong = 0
for row in A:
    tong += sum(row)
print("Tổng các phần tử:", tong)