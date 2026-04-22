def dao_nguoc_danh_sach(danh_sach):
    n = len(danh_sach)
    danh_sach_dao = []
    for i in range(n - 1, -1, -1):
        danh_sach_dao.append(danh_sach[i])
    return danh_sach_dao
 
 
# Nhập danh sách từ bàn phím
chuoi_nhap = input("Nhập các phần tử của danh sách (cách nhau bằng dấu cách): ")
danh_sach = chuoi_nhap.split()
 
# Chuyển về số nguyên nếu có thể, nếu không giữ nguyên chuỗi
danh_sach_xu_ly = []
for x in danh_sach:
    try:
        danh_sach_xu_ly.append(int(x))
    except ValueError:
        danh_sach_xu_ly.append(x)
 
print(f"Danh sách ban đầu : {danh_sach_xu_ly}")
 
ket_qua = dao_nguoc_danh_sach(danh_sach_xu_ly)
print(f"Danh sách đảo ngược: {ket_qua}")
 