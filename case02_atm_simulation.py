balance = float(input("Enter initial balance: "))
n = int(input("How many transactions? "))
deposits = 0
withdrawals = 0
rejected = 0

if balance < 0 or n < 0:
    print("Invalid starting balance or transaction count.")
else:
    for i in range(n):
        kind = input("Enter D for deposit or W for withdrawal: ").upper()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount. Transaction rejected.")
            rejected += 1
        elif kind == "D":
            balance += amount
            deposits += 1
            print("Deposit successful.")
        elif kind == "W":
            if amount <= balance:
                balance -= amount
                withdrawals += 1
                print("Withdrawal successful.")
            else:
                print("Insufficient balance. Transaction rejected.")
                rejected += 1
        else:
            print("Invalid transaction type.")
            rejected += 1

    print("\nTransaction Summary")
    print("Final balance:", round(balance, 2))
    print("Successful deposits:", deposits)
    print("Successful withdrawals:", withdrawals)
    print("Rejected transactions:", rejected)
