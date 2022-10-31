def pass_validator(password):
    condition = True
    if 6 > len(password) or len(password) > 10:
        condition = False
        print(f"Password must be between 6 and 10 characters")
    if not password.isalnum():
        condition = False
        print(f"Password must consist only of letters and digits")
    counter = 0
    for ch in password:
        if ch.isdigit():
            counter += 1
    if counter < 2:
        condition = False
        print(f"Password must have at least 2 digits")
    if condition:
        print(f"Password is valid")

example_pass = input()
pass_validator(example_pass)
