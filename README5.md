# Case Study 5: String-Based Examination Answer Evaluation

## Problem Statement
Compare multiple-choice answers with an answer key and calculate correct, incorrect, unanswered, and final marks using a specified negative-marking rule.

## Objectives
- Compare student answers with the answer key.
- Count correct, incorrect, and unanswered questions.
- Calculate a score after negative marking.

## Assumptions
- Answers are entered as A, B, C, D, or a dash (-) for unanswered.
- Each correct answer earns 1 mark and each incorrect answer loses 0.25 mark.
- This is a sample policy for the exercise.

## Algorithm
1. Start and define the answer key.
2. Input student answers separated by spaces.
3. Check that the number of answers matches the key.
4. Compare each answer with the key.
5. Count correct, incorrect, and unanswered answers.
6. Calculate score and print the result.

## Flowchart (text version)

```text
Start
Set answer key
Input student answers
Count matches and blanks
Calculate score
Print result
End
```

## Pseudocode

```text
BEGIN
SET key
INPUT answers
IF answer count differs from key THEN PRINT error
ELSE
  SET correct, incorrect, blank to 0
  FOR each answer
    IF answer is '-' THEN blank++
    ELSE IF answer matches key THEN correct++
    ELSE incorrect++
  score = correct - incorrect * 0.25
  PRINT counts and score
END
```

## Python Source Code

```python
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
```

## Test Cases
- Input/scenario: A C B D A. Expected result: 5 correct; score 5.0
- Input/scenario: A B - D C. Expected result: 2 correct, 2 incorrect, 1 unanswered; score 1.5

## Sample Output

```text
Enter 5 answers separated by spaces (use - for blank): A B - D C
Correct answers: 2
Incorrect answers: 2
Unanswered questions: 1
Final score: 1.5 out of 5
```

## Conclusion
The program evaluates answers and calculates the final score using the stated marking policy.
