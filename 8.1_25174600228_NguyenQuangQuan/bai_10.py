def in_uoc_so():
    n = int(input("Nhap so nguyen duong n: "))
    if n <= 0:
        print("n phai la so nguyen duong!")
        return
    print(f"Cac uoc so cua {n}:", end=" ")
    dau_tien = True
    for i in range(1, n + 1):
        if n % i == 0:
            if dau_tien:
                print(i, end="")
                dau_tien = False
            else:
                print(f", {i}", end="")
    print()
 
 
in_uoc_so()