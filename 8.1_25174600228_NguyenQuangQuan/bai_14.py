n = int(input("Nhap so phan tu n: "))
ds = []
for i in range(n):
    x = int(input(f"  Phan tu thu {i+1}: "))
    ds.append(x)
 
# Dung map va lambda tao list binh phuong
ds_binh_phuong = list(map(lambda x: x * x, ds))
 
print(f"Danh sach goc    : {ds}")
print(f"Danh sach binh phuong: {ds_binh_phuong}")