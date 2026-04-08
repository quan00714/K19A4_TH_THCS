n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

squares = [i**2 for i in range(1, n + 1)]

if m >= n:
    print([])
else:
    print(squares[m:])