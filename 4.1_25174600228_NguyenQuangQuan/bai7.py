def menu():
    while True:
        print("\n1.Cong  2.Tru  3.Nhan  4.Chia  0.Thoat")
        chon = int(input("Chon: "))

        if chon == 0:
            break

        a = float(input("a = "))
        b = float(input("b = "))

        if chon == 1:
            print("=", a + b)
        elif chon == 2:
            print("=", a - b)
        elif chon == 3:
            print("=", a * b)
        elif chon == 4:
            print("=" if b != 0 else "Loi", a / b if b != 0 else "")

menu()