# Case Study 10: Advanced Numeric Pattern Generator

## Problem Statement
Generate a hollow diamond pattern based on a user-specified size and reject invalid dimensions.

## Objectives
- Practice nested loops.
- Print a symmetric hollow diamond.
- Validate the size entered by the user.

## Assumptions
- The size must be an integer from 2 to 20.
- The diamond is made using asterisks.

## Algorithm
1. Start and input size.
2. If size is outside the allowed range, print an error.
3. Print the upper half using spaces and boundary asterisks.
4. Print the lower half in reverse order.
5. Stop.

## Flowchart (text version)

```text
Start
Input size
Size valid?
Print upper half
Print lower half
End
```

## Pseudocode

```text
BEGIN
INPUT n
IF n < 2 OR n > 20 THEN PRINT error
ELSE
  FOR i from 1 to n
    PRINT leading spaces and hollow row
  FOR i from n-1 down to 1
    PRINT leading spaces and hollow row
END
```

## Python Source Code

```python
n = int(input("Enter diamond size (2-20): "))

if n < 2 or n > 20:
    print("Please enter a size between 2 and 20.")
else:
    for i in range(1, n + 1):
        spaces = n - i
        if i == 1:
            print(" " * spaces + "*")
        else:
            inside_spaces = 2 * i - 3
            print(" " * spaces + "*" + " " * inside_spaces + "*")

    for i in range(n - 1, 0, -1):
        spaces = n - i
        if i == 1:
            print(" " * spaces + "*")
        else:
            inside_spaces = 2 * i - 3
            print(" " * spaces + "*" + " " * inside_spaces + "*")
```

## Test Cases
- Input/scenario: 3. Expected result:   *\n * *\n*   *\n * *\n  *
- Input/scenario: 1. Expected result: Please enter a size between 2 and 20.

## Sample Output

```text
Enter diamond size (2-20): 3
  *
 * *
*   *
 * *
  *
```

## Conclusion
The program uses nested loops and conditions to print a hollow diamond and validate its size.
