# Case Study 9: Smart Canteen Order and Stock Management

## Problem Statement
Process customer canteen orders, calculate bills, update stock, reject unavailable quantities, and summarize sales and remaining stock.

## Objectives
- Accept orders for menu items.
- Prevent sales beyond available stock.
- Calculate revenue and remaining stock.

## Assumptions
- The sample menu contains three items.
- Each order specifies an item number and quantity.
- Only positive quantities are accepted.

## Algorithm
1. Start and define menu prices and stock.
2. Display the menu and ask for the number of orders.
3. For each order, validate item number and quantity.
4. If stock is sufficient, calculate the bill, update stock, and add to sales.
5. Otherwise reject the order.
6. Print total sales and remaining stock.

## Flowchart (text version)

```text
Start
Create menu and stock
Input number of orders
Read item and quantity
Valid and in stock?
Calculate bill and update stock or reject
More orders?
Print sales and stock
End
```

## Pseudocode

```text
BEGIN
SET menu, prices, stock
INPUT n
REPEAT n times
  INPUT item_number, quantity
  IF item or quantity invalid THEN reject
  ELSE IF quantity > stock THEN reject
  ELSE bill = price * quantity; reduce stock; add to sales
PRINT total sales and remaining stock
END
```

## Python Source Code

```python
items = ["Sandwich", "Samosa", "Juice"]
prices = [50, 15, 25]
stock = [10, 20, 12]
total_sales = 0

print("Canteen Menu")
for i in range(len(items)):
    print(i + 1, items[i], "- Rs.", prices[i], "| Stock:", stock[i])

orders = int(input("Enter number of orders: "))

for i in range(orders):
    item_number = int(input("Enter item number (1-3): "))
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
```

## Test Cases
- Input/scenario: Order item 1 quantity 2. Expected result: Order accepted; bill Rs. 100; sandwich stock becomes 8.

## Sample Output

```text
Canteen Menu
1 Sandwich - Rs. 50 | Stock: 10
2 Samosa - Rs. 15 | Stock: 20
3 Juice - Rs. 25 | Stock: 12
Enter number of orders: 1
Enter item number (1-3): 1
Enter quantity: 2
Order accepted. Bill: Rs. 100
Daily Sales: Rs. 100
Remaining Stock:
Sandwich : 8
Samosa : 20
Juice : 12
```

## Conclusion
The canteen program calculates bills, updates inventory, rejects unavailable orders, and reports sales.
