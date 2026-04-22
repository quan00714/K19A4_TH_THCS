def doc_ascii():
    print("Nhap ky tu de xem gia tri ASCII.")
    print("Nhap 'ESC' (chu hoa) hoac de trong roi Enter de thoat.\n")
    while True:
        ky_tu = input("Nhap ky tu: ")
        if ky_tu == "" or ky_tu.upper() == "ESC":
            print("Da thoat chuong trinh.")
            break
        c = ky_tu[0]
        print(f"Ky tu '{c}' co gia tri ASCII = {ord(c)}")
 
 
doc_ascii()