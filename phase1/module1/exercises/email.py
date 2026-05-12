import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Email = ")

print("Your email is valid") if is_valid_email(email) else print("Your email is invalid")
