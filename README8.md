# Case Study 8: Food Waste Monitoring System

## Problem Statement
Compare meals prepared, meals served, and leftovers over several days, calculate wastage percentages, and identify days exceeding an allowed limit.

## Objectives
- Calculate leftover meals.
- Calculate wastage percentage.
- Flag days where wastage exceeds the threshold.

## Assumptions
- Prepared meals must be greater than zero.
- Served meals cannot exceed prepared meals.
- The example threshold is 10 percent.

## Algorithm
1. Start and define daily prepared and served meal counts.
2. For each day, calculate leftovers.
3. Calculate wastage percentage using prepared meals as the base.
4. Compare percentage with the allowed threshold.
5. Print each day's report and flag excessive waste.

## Flowchart (text version)

```text
Start
Input daily meal counts
Validate counts
Calculate leftovers and percentage
Above threshold?
Print daily report
End
```

## Pseudocode

```text
BEGIN
SET threshold = 10
FOR each day
  INPUT prepared, served
  IF prepared <= 0 OR served < 0 OR served > prepared THEN report invalid
  ELSE leftovers = prepared - served
    waste_percent = leftovers / prepared * 100
    PRINT daily report
    IF waste_percent > threshold THEN PRINT warning
END
```

## Python Source Code

```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared_meals = [100, 120, 90, 110, 100]
served_meals = [92, 100, 85, 90, 70]
threshold = 10

for i in range(len(days)):
    prepared = prepared_meals[i]
    served = served_meals[i]

    if prepared <= 0 or served < 0 or served > prepared:
        print(days[i], "- Invalid meal counts")
    else:
        leftovers = prepared - served
        waste_percent = leftovers / prepared * 100
        print(days[i], "leftovers:", leftovers,
              "wastage:", round(waste_percent, 2), "%")
        if waste_percent > threshold:
            print("  Warning: Wastage exceeded", threshold, "%")
```

## Test Cases
- Input/scenario: Monday: 100 prepared, 92 served. Expected result: 8 leftovers; 8% wastage; no warning.
- Input/scenario: Friday: 100 prepared, 70 served. Expected result: 30 leftovers; 30% wastage; warning.

## Sample Output

```text
Monday leftovers: 8 wastage: 8.0 %
Tuesday leftovers: 20 wastage: 16.67 %
  Warning: Wastage exceeded 10 %
Wednesday leftovers: 5 wastage: 5.56 %
Thursday leftovers: 20 wastage: 18.18 %
  Warning: Wastage exceeded 10 %
Friday leftovers: 30 wastage: 30.0 %
  Warning: Wastage exceeded 10 %
```

## Conclusion
The program monitors daily leftovers and highlights days with food wastage above the chosen limit.
