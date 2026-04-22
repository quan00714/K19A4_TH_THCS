def fibonacci():
    so_hang = int(input("Nhap so hang can in (toi da 20): "))
 
    if so_hang <= 0:
        print("So hang phai lon hon 0.")
        return
    if so_hang > 20:
        so_hang = 20
        print("Vuot qua 20, chi in 20 so hang.")
 
    a, b = 0, 1
    print("Day Fibonacci:", end=" ")
    for i in range(so_hang):
        if i < so_hang - 1:
            print(a, end=", ")
        else:
            print(a)
        a, b = b, a + b
 
 
fibonacci()
 