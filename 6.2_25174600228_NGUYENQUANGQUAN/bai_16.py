n = int(input("Nhập n: "))
matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for row in matrix:
    print(row)