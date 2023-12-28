def check_password():
    password = input("Create a password for your bank account: ")
    if len(password) < 8:
        print("Your password is too short. It must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Your password must contain at least one uppercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Your password must contain at least one digit.")
    else:
        print("Your password is valid.")

check_password()