# ----- a) Uoc chung lon nhat -----
def ucln(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
 
 
# ----- b) Boi chung nho nhat -----
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
 
 
# ----- c) Rut gon phan so -----
def rut_gon_phan_so():
    tu  = int(input("Nhap tu so: "))
    mau = int(input("Nhap mau so: "))
    if mau == 0:
        print("Mau so khong duoc bang 0!")
        return
    uoc = ucln(abs(tu), abs(mau))
    tu_rg  = tu  // uoc
    mau_rg = mau // uoc
    if mau_rg < 0:
        tu_rg, mau_rg = -tu_rg, -mau_rg
    print(f"Phan so sau rut gon: {tu_rg}/{mau_rg}")
 
 
# ----- d) Tim min va max trong n so nguyen -----
def tim_min_max():
    n = int(input("Nhap so luong phan tu n: "))
    if n <= 0:
        print("n phai lon hon 0.")
        return
    ds = []
    for i in range(n):
        x = int(input(f"  Phan tu thu {i+1}: "))
        ds.append(x)
    so_min = ds[0]
    so_max = ds[0]
    for x in ds:
        if x < so_min:
            so_min = x
        if x > so_max:
            so_max = x
    print(f"Nho nhat: {so_min}")
    print(f"Lon nhat: {so_max}")
 
 
# ----- Chay chuong trinh -----
print("=== a) UCLN ===")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"UCLN({a}, {b}) = {ucln(a, b)}")
 
print("\n=== b) BCNN ===")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"BCNN({a}, {b}) = {bcnn(a, b)}")
 
print("\n=== c) Rut gon phan so ===")
rut_gon_phan_so()
 
print("\n=== d) Tim min va max ===")
tim_min_max()