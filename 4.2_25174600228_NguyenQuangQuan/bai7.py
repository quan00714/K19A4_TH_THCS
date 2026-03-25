def hien_thi_menu():
    """Hiển thị menu đồ uống"""
    print("\n" + "="*40)
    print("               MENU ĐỒ UỐNG")
    print("="*40)
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    print("0. Thoát")
    print("="*40)

def lay_ten_mon(ma_mon):
    """Lấy tên món dựa vào mã số"""
    menu = {
        1: "Cafe",
        2: "Cam vắt",
        3: "Nước ép cà rốt",
        4: "Nước lọc",
        5: "Nước dừa"
    }
    return menu.get(ma_mon, "Không hợp lệ")

def cach_1_while():
    """Cách 1: Sử dụng while để lặp chọn đồ uống"""
    print("\n=== CÁCH 1: DÙNG WHILE LẶP CHỌN ĐỒ UỐNG ===")
    
    don_hang = []
    
    while True:
        hien_thi_menu()
        try:
            lua_chon = int(input("Vui lòng chọn đồ uống (0 để thoát): "))
            
            if lua_chon == 0:
                break
            elif 1 <= lua_chon <= 5:
                ten_mon = lay_ten_mon(lua_chon)
                don_hang.append(ten_mon)
                print(f"Đã thêm {ten_mon} vào đơn hàng!")

                while True:
                    tiep = input("Bạn có muốn gọi thêm không? (c/k): ").strip().lower()
                    if tiep in ['c', 'k']:
                        break
                    print("Vui lòng nhập 'c' để tiếp tục hoặc 'k' để kết thúc!")
                
                if tiep == 'k':
                    break
            else:
                print("Vui lòng chọn từ 0 đến 5!")
        except ValueError:
            print("Vui lòng nhập số!")
    if don_hang:
        print("\n" + "="*40)
        print("               ĐƠN HÀNG CỦA BẠN")
        print("="*40)
        for i, mon in enumerate(don_hang, 1):
            print(f"{i}. {mon}")
        print(f"Tổng số món: {len(don_hang)}")
    else:
        print("Bạn chưa gọi món nào!")

def cach_2_for():
    """Cách 2: Sử dụng for với số lần gọi giới hạn"""
    print("\n=== CÁCH 2: DÙNG FOR GIỚI HẠN SỐ LẦN GỌI ===")
    
    don_hang = []
    max_mon = 10  
    
    for lan in range(1, max_mon + 1):
        hien_thi_menu()
        print(f"Lần gọi thứ {lan} (tối đa {max_mon} món)")
        
        try:
            lua_chon = int(input("Vui lòng chọn đồ uống (0 để kết thúc): "))
            
            if lua_chon == 0:
                break
            elif 1 <= lua_chon <= 5:
                ten_mon = lay_ten_mon(lua_chon)
                don_hang.append(ten_mon)
                print(f"Đã thêm {ten_mon} vào đơn hàng!")
            else:
                print("Vui lòng chọn từ 0 đến 5!")
                continue
        except ValueError:
            print("Vui lòng nhập số!")
            continue

        if lan == max_mon:
            print("Đã đạt giới hạn số món tối đa!")
    
    if don_hang:
        print("\n" + "="*40)
        print("               ĐƠN HÀNG CỦA BẠN")
        print("="*40)
        for i, mon in enumerate(don_hang, 1):
            print(f"{i}. {mon}")
        print(f"Tổng số món: {len(don_hang)}")
    else:
        print("Bạn chưa gọi món nào!")
cach_1_while()
cach_2_for()
