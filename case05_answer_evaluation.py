answer_key = ["A", "C", "B", "D", "A"]
answers = input("Enter 5 answers separated by spaces (use - for blank): ").upper().split()

if len(answers) != len(answer_key):
    print("Please enter exactly", len(answer_key), "answers.")
else:
    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(len(answer_key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == answer_key[i]:
            correct += 1
        else:
            incorrect += 1

    score = correct - incorrect * 0.25
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered questions:", unanswered)
    print("Final score:", round(score, 2), "out of", len(answer_key))
