# Case Study 6: Student Marks Matrix Analysis

## Problem Statement
Store marks for several students and subjects in a nested list, calculate student totals and subject averages, and find the top performer.

## Objectives
- Represent marks as a nested list.
- Calculate totals and averages.
- Identify the student with the highest total.

## Assumptions
- The example has three students and three subjects.
- Marks are between 0 and 100.
- Each subject has equal importance.

## Algorithm
1. Start and define student names, subject names, and the marks matrix.
2. Calculate each student's total.
3. Calculate each subject's average.
4. Find the student with the highest total.
5. Print totals, averages, and top performer.

## Flowchart (text version)

```text
Start
Create marks matrix
Calculate row totals
Calculate column averages
Find highest total
Display results
End
```

## Pseudocode

```text
BEGIN
SET students, subjects, marks matrix
FOR each student row
  CALCULATE row total
FOR each subject column
  CALCULATE column average
FIND maximum student total
PRINT totals, averages, top student
END
```

## Python Source Code

```python
students = ["Asha", "Ravi", "Sara"]
subjects = ["Python", "Maths", "English"]
marks = [
    [85, 78, 90],
    [72, 88, 80],
    [92, 91, 89]
]

totals = []
for i in range(len(marks)):
    total = sum(marks[i])
    totals.append(total)
    print(students[i], "total:", total, "average:", round(total / len(subjects), 2))

print("\nSubject averages:")
for j in range(len(subjects)):
    column_total = 0
    for i in range(len(marks)):
        column_total += marks[i][j]
    print(subjects[j], ":", round(column_total / len(students), 2))

top_index = totals.index(max(totals))
print("Top performer:", students[top_index], "with", totals[top_index], "marks")
```

## Test Cases
- Input/scenario: Built-in example. Expected result: Asha total 253; Ravi total 240; Sara total 272; Sara is top performer.

## Sample Output

```text
Asha total: 253 average: 84.33
Ravi total: 240 average: 80.0
Sara total: 272 average: 90.67
Subject averages:
Python : 83.0
Maths : 85.67
English : 86.33
Top performer: Sara with 272 marks
```

## Conclusion
The nested-list program summarizes student marks and identifies the top performer and subject averages.
