# ----- a) Kiem tra so nguyen to -----
def kiem_tra_nguyen_to():
    n = int(input("Nhap so nguyen duong n: "))
    if n < 2:
        print(f"{n} khong phai so nguyen to.")
        return
    la_nguyen_to = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_nguyen_to = False
            break
        i += 1
    if la_nguyen_to:
        print(f"{n} la so nguyen to.")
    else:
        print(f"{n} khong phai so nguyen to.")
 
 
# ----- b) Kiem tra so hoan hao -----
def kiem_tra_hoan_hao():
    n = int(input("Nhap so nguyen duong n: "))
    if n <= 0:
        print("n phai lon hon 0.")
        return
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(f"{n} la so hoan hao.")
    else:
        print(f"{n} khong phai so hoan hao.")
 
 
# ----- c) In cac so doi xung trong pham vi 1000 -----
def la_doi_xung(n):
    s = str(n)
    do_dai = len(s)
    for i in range(do_dai // 2):
        if s[i] != s[do_dai - 1 - i]:
            return False
    return True
 
 
def in_so_doi_xung():
    print("Cac so doi xung tu 1 den 1000:")
    dem = 0
    for i in range(1, 1001):
        if la_doi_xung(i):
            print(f"{i:5}", end="")
            dem += 1
            if dem % 15 == 0:
                print()
    print()
 
 
# ----- Chay chuong trinh -----
print("=== a) Kiem tra so nguyen to ===")
kiem_tra_nguyen_to()
 
print("\n=== b) Kiem tra so hoan hao ===")
kiem_tra_hoan_hao()
 
print("\n=== c) So doi xung trong pham vi 1000 ===")
in_so_doi_xung()