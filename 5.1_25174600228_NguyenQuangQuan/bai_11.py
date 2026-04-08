test_list = [(4, 5), (7, 6), (1, 0), (3, 4)]
search_tup = [(3, 4), (8, 9), (7, 6), (1, 2)]

common = [t for t in search_tup if t in test_list]

print("test_list:", test_list)
print("search_tup:", search_tup)
print("Các tuple trong search_tup có trong test_list:", common)