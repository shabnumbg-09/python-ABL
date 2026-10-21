# Case Study 4: Password Policy Validation Engine

## Problem Statement
Check a sample password against minimum length and character-category requirements and explain which rules are not satisfied.

## Objectives
- Check password length.
- Check uppercase, lowercase, digit, and special character presence.
- Report all failed conditions.

## Assumptions
- The password is sample input for this educational program.
- A valid password has at least 8 characters and contains uppercase, lowercase, digit, and special character.

## Algorithm
1. Start and input a sample password.
2. Check its length and character categories.
3. Store each failed rule in a list.
4. If no rules failed, print valid; otherwise print invalid and list the failed rules.
5. Stop.

## Flowchart (text version)

```text
Start
Input sample password
Check all rules
Any failed rules?
Print valid or failed rules
End
```

## Pseudocode

```text
BEGIN
INPUT password
SET errors to empty list
IF length < 8 THEN add length error
IF no uppercase THEN add uppercase error
IF no lowercase THEN add lowercase error
IF no digit THEN add digit error
IF no special character THEN add special-character error
IF errors empty THEN PRINT valid ELSE PRINT errors
END
```

## Python Source Code

```python
password = input("Enter a sample password to check: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters.")
if not any(ch.isupper() for ch in password):
    errors.append("Add at least one uppercase letter.")
if not any(ch.islower() for ch in password):
    errors.append("Add at least one lowercase letter.")
if not any(ch.isdigit() for ch in password):
    errors.append("Add at least one digit.")
if not any(not ch.isalnum() for ch in password):
    errors.append("Add at least one special character.")

if len(errors) == 0:
    print("Password meets all sample rules.")
else:
    print("Password does not meet the sample rules:")
    for error in errors:
        print("-", error)
```

## Test Cases
- Input/scenario: Abc@1234. Expected result: Meets all sample rules.
- Input/scenario: hello. Expected result: Reports missing length, uppercase, digit, and special character.

## Sample Output

```text
Enter a sample password to check: hello
Password does not meet the sample rules:
- Use at least 8 characters.
- Add at least one uppercase letter.
- Add at least one digit.
- Add at least one special character.
```

## Conclusion
The program validates a sample password and explains which policy requirements are missing.
