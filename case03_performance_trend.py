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
