def la_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    return False
 
 
def so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        return "Tháng không hợp lệ (phải từ 1 đến 12)"
 
    # Các tháng có 31 ngày
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
 
    # Các tháng có 30 ngày
    if thang in [4, 6, 9, 11]:
        return 30
 
    # Tháng 2
    if thang == 2:
        if la_nam_nhuan(nam):
            return 29
        else:
            return 28
 
 
# Nhập từ bàn phím
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
 
so_ngay = so_ngay_trong_thang(thang, nam)
print(f"Tháng {thang} năm {nam} có {so_ngay} ngày")
 