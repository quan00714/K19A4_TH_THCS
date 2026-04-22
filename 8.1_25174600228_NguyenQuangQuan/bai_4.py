# ----- a) P(n) = 1 x 3 x 5 x ... x (2n+1), n >= 0 -----
def tinh_P_a(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich
 
 
# ----- b) S(n) = 1 - 2 + 3 - 4 + ... + (-1)^(n+1)*n, n >= 0 -----
def tinh_S_b(n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong += i
        else:
            tong -= i
    return tong
 
 
# ----- c) S(n) = 1 + (1+2) + (1+2+3) + ... + (1+2+...+n) -----
def tinh_S_c(n):
    tong = 0
    for i in range(1, n + 1):
        tong_con = 0
        for j in range(1, i + 1):
            tong_con += j
        tong += tong_con
    return tong
 
 
# ----- d) P(x,y) = x^y + sum_{k=1}^{n}(x + 3^(2y) + y^k), n > 1 -----
def tinh_P_d(x, y, n):
    tong = luy_thua(x, y)
    for k in range(1, n + 1):
        tong += x + luy_thua(3, 2 * y) + luy_thua(y, k)
    return tong
 
 
# ----- Chay chuong trinh -----
print("=== a) P(n) = 1 x 3 x 5 x ... x (2n+1) ===")
n = int(input("Nhap n (n >= 0): "))
print(f"P({n}) = {tinh_P_a(n)}")
 
print("\n=== b) S(n) = 1 - 2 + 3 - 4 + ... ===")
n = int(input("Nhap n (n >= 0): "))
print(f"S({n}) = {tinh_S_b(n)}")
 
print("\n=== c) S(n) = 1 + (1+2) + (1+2+3) + ... ===")
n = int(input("Nhap n (n >= 0): "))
print(f"S({n}) = {tinh_S_c(n)}")
 
print("\n=== d) P(x,y) = x^y + sum(x + 3^(2y) + y^k) ===")
x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
n = int(input("Nhap n (n > 1): "))
if n <= 1:
    print("n phai lon hon 1!")
else:
    print(f"P({x},{y}) voi n={n} = {tinh_P_d(x, y, n)}")