import re

password = input("Enter your password: ")

if len(password) < 8:
    print("Too short!")
elif not re.search(r"\d", password):
    print("Add at least one number.")
elif not re.search(r"[A-Z]", password):
    print("Add at least one uppercase letter.")
elif not re.search(r"[a-z]", password):
    print("Add at least one lowercase letter.")
else:
    print("Strong password!")