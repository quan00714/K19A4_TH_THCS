def cong(a, b):  return a + b
def tru(a, b):   return a - b
def nhan(a, b):  return a * b
 
def chia(a, b):
    if b == 0:
        print("Loi: Khong the chia cho 0!")
        return None
    return a / b
 
 
def luy_thua(co_so, mu):
    if mu == 0:
        return 1
    ket_qua = 1
    for _ in range(int(abs(mu))):
        ket_qua *= co_so
    return (1 / ket_qua) if mu < 0 else ket_qua
 
 
# ----- a^(b+n) va b^(n+2)/a -----
def tinh_luy_thua_nang_cao(a, b, n):
    print(f"a^(b+n) = {a}^({b}+{n}) = {luy_thua(a, b + n)}")
    if a == 0:
        print("Khong tinh duoc b^(n+2)/a vi a = 0!")
        return
    print(f"b^(n+2)/a = {b}^({n}+2)/{a} = {luy_thua(b, n + 2) / a}")
 
 
# ----- Chay chuong trinh -----
print("=== Phep tinh so hoc ===")
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
print(f"a + b = {cong(a, b)}")
print(f"a - b = {tru(a, b)}")
print(f"a x b = {nhan(a, b)}")
kq = chia(a, b)
if kq is not None:
    print(f"a / b = {kq}")
 
print("\n=== Luy thua nang cao ===")
n = float(input("Nhap n: "))
a2 = float(input("Nhap a: "))
b2 = float(input("Nhap b: "))
tinh_luy_thua_nang_cao(a2, b2, n)