stock = [
    ('macbook air', 99, '13-inch'),
    ('dell inspiron', 55, '15-inch'),
    ('dell xps', 20, '13-inch'),
    ('macbook pro', 15, '16-inch'),
    ('dell latitude', 8, '15-inch')
]

stock_products = list(map(lambda item:item[0].title(), stock))
print(stock_products)

