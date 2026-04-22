# ----- a) List so chan trong khoang dong [1, 100] -----
so_chan = list(filter(lambda x: x % 2 == 0, range(1, 101)))
print("=== a) So chan trong [1, 100] ===")
print(so_chan)
 
# ----- b) Tong so chan trong danh sach 1..n dung filter va reduce -----
 
# Ham reduce tu xay dung (khong dung thu vien)
def my_reduce(ham, ds):
    if len(ds) == 0:
        return None
    ket_qua = ds[0]
    for i in range(1, len(ds)):
        ket_qua = ham(ket_qua, ds[i])
    return ket_qua
 
 
print("\n=== b) Tong so chan trong danh sach 1..n ===")
n = int(input("Nhap n: "))
danh_sach = list(range(1, n + 1))
 

so_chan_loc = list(filter(lambda x: x % 2 == 0, danh_sach))

if len(so_chan_loc) == 0:
    tong = 0
else:
    tong = my_reduce(lambda a, b: a + b, so_chan_loc)
 
print(f"Danh sach: {danh_sach}")
print(f"So chan  : {so_chan_loc}")
print(f"Tong so chan: {tong}")