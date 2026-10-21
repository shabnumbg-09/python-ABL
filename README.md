# Case Study 2: ATM Transaction Sequence Simulation

## Problem Statement
Simulate deposits and withdrawals, update an account balance, reject invalid transactions, and show a transaction summary.

## Objectives
- Process a sequence of transactions.
- Prevent withdrawals above the available balance.
- Display the final balance and transaction counts.

## Assumptions
- The account starts with a non-negative balance.
- Enter transaction type as D for deposit or W for withdrawal.
- Transactions use positive amounts.

## Algorithm
1. Start and read the initial balance.
2. Read the number of transactions.
3. Repeat for each transaction: read type and amount.
4. Accept a positive deposit; allow a withdrawal only if funds are sufficient.
5. Count accepted deposits and withdrawals; report rejected transactions.
6. Print final balance and summary.

## Flowchart (text version)

```text
Start
Input balance and transaction count
Read transaction
Valid deposit?
Valid withdrawal?
Update balance or reject
More transactions?
Print summary
End
```

## Pseudocode

```text
BEGIN
INPUT balance, n
REPEAT n times
  INPUT type, amount
  IF amount <= 0 THEN PRINT invalid
  ELSE IF type = D THEN balance = balance + amount
  ELSE IF type = W AND amount <= balance THEN balance = balance - amount
  ELSE PRINT transaction rejected
END REPEAT
PRINT balance and summary
END
```

## Python Source Code

```python
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
```

## Test Cases
- Input/scenario: 1000;D;500;W;200. Expected result: Final balance: 1300.0 for a deposit of 500 and withdrawal of 200.

## Sample Output

```text
Enter initial balance: 1000
How many transactions? 2
Enter D for deposit or W for withdrawal: D
Enter amount: 500
Deposit successful.
Enter D for deposit or W for withdrawal: W
Enter amount: 200
Withdrawal successful.
Transaction Summary
Final balance: 1300.0
```

## Conclusion
The simulation updates the balance safely and summarizes successful and rejected transactions.
