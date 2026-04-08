m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tup = tuple(range(m, n + 1))
mid = len(tup) // 2

tp1 = tup[:mid]
tp2 = tup[mid:]

print("tp1:", tp1)
print("tp2:", tp2)