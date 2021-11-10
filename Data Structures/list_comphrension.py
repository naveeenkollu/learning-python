stock = [
    ('macbook air', 99, '13-inch', 999),
    ('dell inspiron', 55, '15-inch', 849),
    ('dell xps', 20, '13-inch', 1500),
    ('macbook pro', 15, '16-inch', 2500),
    ('dell latitude', 8, '15-inch', 1250)
]

# List comphrension way of filtering
filtered  = [price[3] for price in stock if price[3] > 999]
print(filtered)

# for price in stock:
#     if price[3] > 999:
#         filtered.append(price[3])

# print(filtered)