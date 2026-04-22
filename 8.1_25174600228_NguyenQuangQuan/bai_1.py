def tinh_luy_thua():
    so = int(input("Nhap so tu nhien: "))
    n  = int(input("Nhap bac n: "))
 
    ket_qua = 1
    for _ in range(n):
        ket_qua *= so
 
    print(f"{so}^{n} = {ket_qua}")
 
 
tinh_luy_thua()