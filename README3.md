# Case Study 3: Student Performance Trend Analysis

## Problem Statement
Compare a student's marks in two examinations, identify improvements and declines, and calculate the overall change.

## Objectives
- Store marks for multiple subjects.
- Compare marks from two examinations.
- Identify subjects that improved, declined, or stayed the same.

## Assumptions
- Marks are between 0 and 100.
- The same subjects appear in both examinations.

## Algorithm
1. Start and input subject names.
2. For each subject, input marks from Exam 1 and Exam 2.
3. Validate marks.
4. Compare each pair of marks and classify the trend.
5. Calculate total marks for both exams and display the results.

## Flowchart (text version)

```text
Start
Input subjects and marks
Marks valid?
Compare each subject
Calculate totals
Display trends
End
```

## Pseudocode

```text
BEGIN
INPUT subject names
FOR each subject
  INPUT mark1, mark2
  IF marks invalid THEN report error
  ELSE compare mark2 with mark1
    IF mark2 > mark1 THEN improved
    ELSE IF mark2 < mark1 THEN declined
    ELSE unchanged
PRINT subject trends and totals
END
```

## Python Source Code

```python
subjects = ["Python", "Maths", "English"]
exam1 = []
exam2 = []

for subject in subjects:
    first = float(input("Enter " + subject + " marks in Exam 1: "))
    second = float(input("Enter " + subject + " marks in Exam 2: "))
    if first < 0 or first > 100 or second < 0 or second > 100:
        print("Marks must be between 0 and 100. Please restart and enter valid marks.")
        break
    exam1.append(first)
    exam2.append(second)
else:
    print("\nPerformance Trend")
    for i in range(len(subjects)):
        if exam2[i] > exam1[i]:
            status = "Improved"
        elif exam2[i] < exam1[i]:
            status = "Declined"
        else:
            status = "No change"
        print(subjects[i], ":", status, "(change:", exam2[i] - exam1[i], ")")

    print("Exam 1 total:", sum(exam1))
    print("Exam 2 total:", sum(exam2))
    print("Overall change:", sum(exam2) - sum(exam1))
```

## Test Cases
- Input/scenario: Python 70,80; Maths 60,55; English 75,75. Expected result: Python improved by 10; Maths declined by 5; English unchanged.

## Sample Output

```text
Python marks: 70, 80
Maths marks: 60, 55
English marks: 75, 75
Python : Improved (change: 10.0 )
Maths : Declined (change: -5.0 )
English : No change (change: 0.0 )
Exam 1 total: 205.0
Exam 2 total: 210.0
Overall change: 5.0
```

## Conclusion
The program compares exam scores and clearly reports subject-wise and overall performance trends.
