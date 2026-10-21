products = [
    ("P101", 50.0, 10),
    ("P102", 120.0, 3),
    ("P103", 75.0, 0),
    ("P104", 40.0, 8)
]

total_value = 0
print("Product Catalogue Audit")

for product in products:
    product_id, price, quantity = product

    if price < 0 or quantity < 0:
        print(product_id, "- Invalid record")
    else:
        value = price * quantity
        total_value += value
        print(product_id, "inventory value:", value)
        if quantity < 5:
            print("  Replenishment needed; current stock:", quantity)

print("Total inventory value:", round(total_value, 2))
