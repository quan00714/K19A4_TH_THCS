# Can bac hai (phuong phap Newton-Raphson, khong dung thu vien)
def can_bac_hai(x):
    if x < 0:
        return None
    if x == 0:
        return 0.0
    guess = x / 2.0
    for _ in range(1000):
        better = (guess + x / guess) / 2.0
        if abs(better - guess) < 1e-10:
            break
        guess = better
    return guess
 
 
# ----- Hinh tron -----
def hinh_tron():
    r = float(input("Ban kinh r: "))
    if r <= 0:
        print("Ban kinh phai lon hon 0!")
        return
    print(f"  Chu vi  = {2 * PI * r:.4f}")
    print(f"  Dien tich = {PI * r * r:.4f}")
 
 
# ----- Hinh vuong -----
def hinh_vuong():
    a = float(input("Canh a: "))
    if a <= 0:
        print("Canh phai lon hon 0!")
        return
    print(f"  Chu vi  = {4 * a:.4f}")
    print(f"  Dien tich = {a * a:.4f}")
 
 
# ----- Hinh chu nhat -----
def hinh_chu_nhat():
    a = float(input("Chieu dai a: "))
    b = float(input("Chieu rong b: "))
    if a <= 0 or b <= 0:
        print("Cac canh phai lon hon 0!")
        return
    print(f"  Chu vi  = {2 * (a + b):.4f}")
    print(f"  Dien tich = {a * b:.4f}")
 
 
# ----- Hinh tam giac -----
def hinh_tam_giac():
    a = float(input("Canh a: "))
    b = float(input("Canh b: "))
    c = float(input("Canh c: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Cac canh phai lon hon 0!")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ba canh khong hop le!")
        return
    s = (a + b + c) / 2
    dt = can_bac_hai(s * (s - a) * (s - b) * (s - c))
    print(f"  Chu vi  = {a + b + c:.4f}")
    print(f"  Dien tich = {dt:.4f}")
 
 
# ----- Chay chuong trinh -----
print("=== Hinh tron ===")
hinh_tron()
print("\n=== Hinh vuong ===")
hinh_vuong()
print("\n=== Hinh chu nhat ===")
hinh_chu_nhat()
print("\n=== Hinh tam giac ===")
hinh_tam_giac()