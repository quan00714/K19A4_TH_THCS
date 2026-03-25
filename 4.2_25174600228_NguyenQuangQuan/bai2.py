def nhap_phan_so_cach1():
    """Cách 1: Sử dụng while"""
    print("\n=== CÁCH 1: DÙNG WHILE KIỂM TRA MẪU SỐ ===")
    while True:
        try:
            tu = int(input("Nhập tử số: "))
            mau = int(input("Nhập mẫu số: "))
            if mau == 0:
                print("Mẫu số không thể bằng 0! Vui lòng nhập lại.")
            else:
                print(f"Phân số: {tu}/{mau}")
                a, b = abs(tu), abs(mau)
                while b != 0:
                    a, b = b, a % b
                ucln = a
                tu_gian = tu // ucln
                mau_gian = mau // ucln
                print(f"Phân số tối giản: {tu_gian}/{mau_gian}")
                break
        except ValueError:
            print("Vui lòng nhập số nguyên!")

def nhap_phan_so_cach2():
    """Cách 2: Sử dụng for """
    print("\n=== CÁCH 2: DÙNG FOR + WHILE KIỂM TRA MẪU SỐ ===")
    max_lan = 5
    for lan in range(1, max_lan + 1):
        try:
            tu = int(input("Nhập tử số: "))
            while True:
                mau = int(input("Nhập mẫu số: "))
                if mau == 0:
                    print("Mẫu số không thể bằng 0! Vui lòng nhập lại.")
                else:
                    break
            print(f"Phân số: {tu}/{mau}")
            
            a, b = abs(tu), abs(mau)
            while b != 0:
                a, b = b, a % b
            ucln = a
            tu_gian = tu // ucln
            mau_gian = mau // ucln
            print(f"Phân số tối giản: {tu_gian}/{mau_gian}")
            return
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    
    print("Đã vượt quá số lần nhập cho phép!")

nhap_phan_so_cach1()
nhap_phan_so_cach2()