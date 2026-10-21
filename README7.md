# Case Study 7: Tuple-Based Product Catalogue Audit

## Problem Statement
Store product IDs, prices, and stock quantities in tuples, calculate inventory values, identify invalid records, and find items needing replenishment.

## Objectives
- Store product details as tuples.
- Calculate total inventory value.
- Identify low-stock items and invalid records.

## Assumptions
- Each product tuple contains ID, price, and quantity.
- A stock quantity below 5 requires replenishment.
- Prices and quantities must not be negative.

## Algorithm
1. Start and create a list of product tuples.
2. Unpack each tuple into ID, price, and quantity.
3. Validate price and quantity.
4. Calculate each inventory value and the overall value.
5. List products with stock below 5.

## Flowchart (text version)

```text
Start
Create product tuples
Unpack product details
Validate values
Calculate inventory value
Check low stock
Print report
End
```

## Pseudocode

```text
BEGIN
SET product tuples
SET total_value = 0
FOR each product tuple
  UNPACK id, price, quantity
  IF price or quantity invalid THEN report invalid
  ELSE total_value += price * quantity
  IF quantity < 5 THEN report replenishment
PRINT total inventory value
END
```

## Python Source Code

```python
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
```

## Test Cases
- Input/scenario: Built-in example. Expected result: P102 and P103 need replenishment; total inventory value 1180.0.

## Sample Output

```text
Product Catalogue Audit
P101 inventory value: 500.0
P102 inventory value: 360.0
  Replenishment needed; current stock: 3
P103 inventory value: 0.0
  Replenishment needed; current stock: 0
P104 inventory value: 320.0
Total inventory value: 1180.0
```

## Conclusion
The program uses tuples and unpacking to audit product stock and calculate inventory value.
