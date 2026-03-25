def nhap_so_lon_hon_100():
    """Nhập số có giá trị > 100, nếu không thỏa mãn thì yêu cầu nhập lại"""
    while True:
        try:
            so = int(input("Nhập số (> 100): "))
            if so > 100:
                return so
            else:
                print("Vui lòng nhập số lớn hơn 100!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

def tong_chu_so_while(so):
    """Tính tổng các chữ số sử dụng while"""
    tong = 0
    so_tam = abs(so) 
    while so_tam > 0:
        tong += so_tam % 10
        so_tam //= 10
    return tong

def tong_chu_so_for(so):
    """Tính tổng các chữ số sử dụng for"""
    tong = 0
    chuoi_so = str(abs(so))
    for ky_tu in chuoi_so:
        tong += int(ky_tu)
    return tong

def cach_1_while():
    """Cách 1: Sử dụng while để nhập và tính tổng"""
    print("\n=== CÁCH 1: DÙNG WHILE NHẬP VÀ TÍNH TỔNG ===")
    
    so = nhap_so_lon_hon_100()
    tong = tong_chu_so_while(so)
    
    print(f"Số đã nhập: {so}")
    print(f"Tổng các chữ số: {tong}")

def cach_2_for():
    """Cách 2: Sử dụng for để tính tổng"""
    print("\n=== CÁCH 2: DÙNG FOR TÍNH TỔNG CÁC CHỮ SỐ ===")
    
    so = nhap_so_lon_hon_100()
    tong = tong_chu_so_for(so)
    
    print(f"Số đã nhập: {so}")
    print(f"Tổng các chữ số: {tong}")
cach_1_while()
cach_2_for()