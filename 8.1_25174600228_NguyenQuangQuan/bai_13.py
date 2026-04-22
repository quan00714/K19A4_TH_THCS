def la_nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
 
 
def so_ngay_trong_thang(m, y):
    if m < 1 or m > 12:
        return -1
    # Thang 30 ngay
    if m in [4, 6, 9, 11]:
        return 30
    # Thang 2
    if m == 2:
        return 29 if la_nam_nhuan(y) else 28
    # Con lai 31 ngay
    return 31
 
 
# ----- Chay chuong trinh -----
y = int(input("Nhap nam: "))
if la_nam_nhuan(y):
    print(f"Nam {y} la nam nhuan.")
else:
    print(f"Nam {y} khong phai nam nhuan.")
 
m = int(input("Nhap thang (1-12): "))
so_ngay = so_ngay_trong_thang(m, y)
if so_ngay == -1:
    print("Thang khong hop le!")
else:
    print(f"Thang {m} nam {y} co {so_ngay} ngay.")