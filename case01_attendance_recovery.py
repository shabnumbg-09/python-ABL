conducted = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid class details.")
elif target < 0 or target > 100:
    print("Target must be between 0 and 100.")
else:
    current = attended / conducted * 100
    extra = 0

    while current < target:
        conducted += 1
        attended += 1
        extra += 1
        current = attended / conducted * 100

    print("Current attendance:", round(attended / conducted * 100, 2), "%")
    if extra == 0:
        print("You have already reached the target.")
    else:
        print("Additional consecutive classes required:", extra)
