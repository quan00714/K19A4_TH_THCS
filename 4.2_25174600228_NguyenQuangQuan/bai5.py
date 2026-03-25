def nhap_so_nguyen(ten_so):
    """Nhập số nguyên, nếu không phải số nguyên thì yêu cầu nhập lại"""
    while True:
        try:
            so = int(input(f"Nhập {ten_so}: "))
            return so
        except ValueError:
            print("Vui lòng nhập số nguyên!")

def ucln_euclid_while(a, b):
    """Tìm UCLN bằng giải thuật Euclid sử dụng vòng lặp while"""
    a_abs = abs(a)
    b_abs = abs(b)
    
    while b_abs != 0:
        a_abs, b_abs = b_abs, a_abs % b_abs
    
    return a_abs

def ucln_euclid_for(a, b):
    """Tìm UCLN bằng giải thuật Euclid sử dụng vòng lặp for (đệ quy)"""
    a_abs = abs(a)
    b_abs = abs(b)

    for _ in range(min(a_abs, b_abs) + 1):
        if b_abs == 0:
            return a_abs
        a_abs, b_abs = b_abs, a_abs % b_abs
        if a_abs == 0:
            return b_abs
    
    return a_abs

def cach_1_while():
    """Cách 1: Sử dụng while để tính UCLN"""
    print("\n=== CÁCH 1: DÙNG WHILE TÍNH UCLN ===")
    
    a = nhap_so_nguyen("số thứ nhất")
    b = nhap_so_nguyen("số thứ hai")
    
    ucln = ucln_euclid_while(a, b)

    if ucln != 0:
        bcnn = abs(a * b) // ucln
        print(f"UCLN({a}, {b}) = {ucln}")
        print(f"BCNN({a}, {b}) = {bcnn}")
    else:
        print("Cả hai số đều bằng 0, BCNN không xác định!")

def cach_2_for():
    """Cách 2: Sử dụng for để tính UCLN"""
    print("\n=== CÁCH 2: DÙNG FOR TÍNH UCLN (MÔ PHỎNG) ===")
    
    a = nhap_so_nguyen("số thứ nhất")
    b = nhap_so_nguyen("số thứ hai")
    
    ucln = ucln_euclid_for(a, b)
    
    if ucln != 0:
        bcnn = abs(a * b) // ucln
        print(f"UCLN({a}, {b}) = {ucln}")
        print(f"BCNN({a}, {b}) = {bcnn}")
    else:
        print("Cả hai số đều bằng 0, BCNN không xác định!")
cach_1_while()
cach_2_for()