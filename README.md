# Case Study 1: Attendance Recovery Computation

## Problem Statement
Calculate a student's current attendance percentage and the minimum number of consecutive classes they must attend to reach a required attendance percentage.

## Objectives
- Calculate current attendance percentage.
- Find the minimum additional classes needed to reach the target.
- Validate the input values.

## Assumptions
- Attended classes cannot exceed conducted classes.
- The target attendance is between 0 and 100 percent.
- All future classes are attended.

## Algorithm
1. Start.
2. Read classes conducted, classes attended, and target percentage.
3. Validate the values.
4. Calculate current attendance percentage.
5. If current attendance already meets the target, print zero additional classes.
6. Otherwise, keep adding one future class to both conducted and attended counts until the target is reached.
7. Print the result and stop.

## Flowchart (text version)

```text
Start
Input C, A, target
Valid inputs?
Calculate percentage
Target reached?
Increase C and A by 1
Print additional classes
End
```

## Pseudocode

```text
BEGIN
INPUT conducted, attended, target
IF inputs are invalid THEN PRINT error
ELSE
  current = attended / conducted * 100
  extra = 0
  WHILE current < target
    conducted = conducted + 1
    attended = attended + 1
    extra = extra + 1
    current = attended / conducted * 100
  END WHILE
  PRINT current, extra
END IF
END
```

## Python Source Code

```python
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
```

## Test Cases
- Input/scenario: 40. Expected result: 75
- Input/scenario: 40. Expected result: 75

## Sample Output

```text
Enter total classes conducted: 40
Enter classes attended: 24
Enter required attendance percentage: 75
Current attendance: 75.0 %
Additional consecutive classes required: 24
```

## Conclusion
The program calculates attendance and determines the number of future classes required to reach the target.
