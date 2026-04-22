import random
 
 
def kiem_tra_chan_le(n):
    # Tạo danh sách n phần tử ngẫu nhiên (từ 1 đến 100)
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ban đầu: {danh_sach}")
 
    # Sử dụng lambda: trả về True nếu số chẵn, False nếu lẻ
    la_chan = lambda x: True if x % 2 == 0 else False
 
    # Áp dụng lambda cho từng phần tử
    ket_qua = list(map(la_chan, danh_sach))
 
    print("\nKết quả kiểm tra chẵn/lẻ:")
    for i in range(len(danh_sach)):
        trang_thai = "Chẵn" if ket_qua[i] else "Lẻ"
        print(f"  {danh_sach[i]} -> {ket_qua[i]} ({trang_thai})")
 
    return ket_qua
 
 
# Nhập từ bàn phím
n = int(input("Nhập độ dài danh sách n: "))
 
ket_qua = kiem_tra_chan_le(n)
 