def nhap_sinh_vien():
    ho_ten   = input("Ho ten sinh vien: ")
    toan     = float(input("Diem Toan: "))
    ly       = float(input("Diem Ly: "))
    hoa      = float(input("Diem Hoa: "))
    return {"ho_ten": ho_ten, "toan": toan, "ly": ly, "hoa": hoa}
 
 
def tinh_trung_binh(sv):
    return (sv["toan"] + sv["ly"] + sv["hoa"]) / 3
 
 
def xuat_sinh_vien(sv):
    tb = tinh_trung_binh(sv)
    print(f"\n--- Thong tin sinh vien ---")
    print(f"Ho ten   : {sv['ho_ten']}")
    print(f"Diem Toan: {sv['toan']}")
    print(f"Diem Ly  : {sv['ly']}")
    print(f"Diem Hoa : {sv['hoa']}")
    print(f"Trung binh: {tb:.2f}")
    if tb >= 8.5:
        print("Xep loai: Gioi")
    elif tb >= 7.0:
        print("Xep loai: Kha")
    elif tb >= 5.0:
        print("Xep loai: Trung binh")
    else:
        print("Xep loai: Yeu")
 
 
sv = nhap_sinh_vien()
xuat_sinh_vien(sv)