import math

def kiem_tra_so_nguyen(x):
    """Kiểm tra xem số có phải số nguyên dương không"""
    if isinstance(x, float) and not x.is_integer():
        return False
    if isinstance(x, int) or (isinstance(x, float) and x.is_integer()):
        if x > 0:
            return True
    return False

def cach_1_while():
    """Cách 1: Sử dụng while vô hạn"""
    print("\n=== CÁCH 1: DÙNG WHILE VÔ HẠN ===")
    print("Nhập số (chương trình dừng khi nhập số âm hoặc số thập phân):")
    
    so_da_nhap = []
    while True:
        try:
            so = input("Nhập số: ")
            if '.' in so:
                so_thuc = float(so)
                print(f"Đã nhập số thập phân: {so_thuc} -> DỪNG CHƯƠNG TRÌNH")
                break
            else:
                so_nguyen = int(so)
                if so_nguyen < 0:
                    print(f"Đã nhập số âm: {so_nguyen} -> DỪNG CHƯƠNG TRÌNH")
                    break
                else:
                    print(f"Đã nhập: {so_nguyen}")
                    so_da_nhap.append(so_nguyen)
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    print(f"Các số đã nhập: {so_da_nhap}")

def cach_2_for():
    """Cách 2: Sử dụng for với giới hạn số lần"""
    print("\n=== CÁCH 2: DÙNG FOR GIỚI HẠN SỐ LẦN NHẬP ===")
    print("Nhập số (chương trình dừng khi nhập số âm hoặc số thập phân):")
    
    so_da_nhap = []
    max_lan = 10
    
    for lan in range(1, max_lan + 1):
        try:
            so = input(f"Lần {lan} - Nhập số: ")
            
            if '.' in so:
                so_thuc = float(so)
                print(f"Đã nhập số thập phân: {so_thuc} -> DỪNG CHƯƠNG TRÌNH")
                break
            else:
                so_nguyen = int(so)
                if so_nguyen < 0:
                    print(f"Đã nhập số âm: {so_nguyen} -> DỪNG CHƯƠNG TRÌNH")
                    break
                else:
                    print(f"Đã nhập: {so_nguyen}")
                    so_da_nhap.append(so_nguyen)
                    if lan == max_lan:
                        print(f"Đã nhập đủ {max_lan} số, không có số âm hoặc thập phân. Kết thúc!")
                        
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    
    print(f"Các số đã nhập: {so_da_nhap}")
cach_1_while()
cach_2_for()