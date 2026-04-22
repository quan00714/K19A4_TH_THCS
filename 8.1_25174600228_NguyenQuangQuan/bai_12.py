LUONG_CO_BAN = 5_000_000   # 5 trieu dong
 
 
def nhap_nhan_vien():
    ho_ten   = input("Ho ten nhan vien: ")
    que_quan = input("Que quan: ")
    tham_nien = int(input("Tham nien cong tac (nam): "))
    if tham_nien < 0:
        tham_nien = 0
    return {"ho_ten": ho_ten, "que_quan": que_quan, "tham_nien": tham_nien}
 
 
def tinh_luong(nv):
    # Phu cap tham nien: 5% luong co ban moi nam cong tac (toi da 50%)
    phan_tram = nv["tham_nien"] * 0.05
    if phan_tram > 0.50:
        phan_tram = 0.50
    return LUONG_CO_BAN + LUONG_CO_BAN * phan_tram
 
 
def xuat_nhan_vien(nv):
    luong = tinh_luong(nv)
    print(f"\n--- Thong tin nhan vien ---")
    print(f"Ho ten      : {nv['ho_ten']}")
    print(f"Que quan    : {nv['que_quan']}")
    print(f"Tham nien   : {nv['tham_nien']} nam")
    print(f"Luong thang : {luong:,.0f} dong")
 
 
nv = nhap_nhan_vien()
xuat_nhan_vien(nv)