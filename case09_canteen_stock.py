items = ["Sandwich", "Samosa", "Juice"]
prices = [50, 15, 25]
stock = [10, 20, 12]
total_sales = 0

print("Canteen Menu")
for i in range(len(items)):
    print(i + 1, items[i], "- Rs.", prices[i], "| Stock:", stock[i])

orders = int(input("Enter number of orders: "))

for i in range(orders):
    item_number = int(input("enter item number(1-3):"))
    quantity = int(input("Enter quantity: "))

    if item_number < 1 or item_number > len(items) or quantity <= 0:
        print("Invalid order.")
    else:
        index = item_number - 1
        if quantity > stock[index]:
            print("Not enough stock. Order rejected.")
        else:
            bill = prices[index] * quantity
            stock[index] -= quantity
            total_sales += bill
            print("Order accepted. Bill: Rs.", bill)

print("\nDaily Sales: Rs.", total_sales)
print("Remaining Stock:")
for i in range(len(items)):
    print(items[i], ":", stock[i])
