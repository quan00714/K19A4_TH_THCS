def so_thanh_chu(so):
    """Chuyển đổi một chữ số thành chữ"""
    chu_so = {
        0: "không", 1: "một", 2: "hai", 3: "ba", 4: "bốn",
        5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"
    }
    return chu_so.get(so, "")

def cach_1_while():
    """Cách 1: Sử dụng while để xử lý từng chữ số"""
    print("\n=== CÁCH 1: DÙNG VÒNG LẶP WHILE ===")
    while True:
        try:
            n = input("Nhập một số: ")
            if n[0] == '-':
                print("Vui lòng nhập số nguyên dương!")
                continue
            so = int(n)
            if so < 0:
                print("Vui lòng nhập số nguyên dương!")
                continue
            ket_qua = []
            so_tam = so
            if so_tam == 0:
                ket_qua.append("không")
            else:
                while so_tam > 0:
                    chu_so_cuoi = so_tam % 10
                    ket_qua.insert(0, so_thanh_chu(chu_so_cuoi))
                    so_tam //= 10
            print(f"{so}: {' '.join(ket_qua)}")
            break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")

def cach_2_for():
    """Cách 2: Sử dụng for để duyệt qua từng ký tự của chuỗi"""
    print("\n=== CÁCH 2: DÙNG VÒNG LẶP FOR ===")
    while True:
        try:
            n = input("Nhập một số: ")
            if n[0] == '-':
                print("Vui lòng nhập số nguyên dương!")
                continue
            so = int(n)
            if so < 0:
                print("Vui lòng nhập số nguyên dương!")
                continue

            ket_qua = []
            for ky_tu in n:
                chu_so = int(ky_tu)
                ket_qua.append(so_thanh_chu(chu_so))
            
            print(f"{so}: {' '.join(ket_qua)}")
            break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
   
cach_1_while()
cach_2_for()