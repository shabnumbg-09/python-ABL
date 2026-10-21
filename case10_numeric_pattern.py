n = int(input("Enter diamond size (2-20): "))

if n < 2 or n > 20:
    print("Please enter a size between 2 and 20.")
else:
    for i in range(1, n + 1):
        spaces = n - i
        if i == 1:
            print(" " * spaces + "*")
        else:
            inside_spaces = 2 * i - 3
            print(" " * spaces + "*" + " " * inside_spaces + "*")

    for i in range(n - 1, 0, -1):
        spaces = n - i
        if i == 1:
            print(" " * spaces + "*")
        else:
            inside_spaces = 2 * i - 3
            print(" " * spaces + "*" + " " * inside_spaces + "*")
