import random
 
 
def tao_danh_sach_va_binh_phuong(n):
    # Tạo danh sách n phần tử ngẫu nhiên (từ 1 đến 100)
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ban đầu: {danh_sach}")
 
    # Sử dụng lambda để tính bình phương các phần tử
    binh_phuong = list(map(lambda x: x ** 2, danh_sach))
    print(f"Bình phương các phần tử: {binh_phuong}")
 
    return danh_sach, binh_phuong
 
 
# Nhập từ bàn phím
n = int(input("Nhập độ dài danh sách n: "))
 
ds, bp = tao_danh_sach_va_binh_phuong(n)