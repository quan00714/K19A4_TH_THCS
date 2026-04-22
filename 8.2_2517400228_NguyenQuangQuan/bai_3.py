import random
 
 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
 
def danh_sach_so_nguyen_to(n):
    # Tạo danh sách n phần tử ngẫu nhiên (từ 1 đến 100)
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ban đầu: {danh_sach}")
 
    # Lọc các số nguyên tố trong danh sách
    cac_so_nguyen_to = []
    for phan_tu in danh_sach:
        if la_so_nguyen_to(phan_tu):
            cac_so_nguyen_to.append(phan_tu)
 
    print(f"Các số nguyên tố trong danh sách: {cac_so_nguyen_to}")
    return cac_so_nguyen_to
 
 
# Nhập từ bàn phím
n = int(input("Nhập độ dài danh sách n: "))
 
danh_sach_so_nguyen_to = danh_sach_so_nguyen_to(n)
 