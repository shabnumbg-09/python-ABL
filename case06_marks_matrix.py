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
