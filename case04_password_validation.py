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
