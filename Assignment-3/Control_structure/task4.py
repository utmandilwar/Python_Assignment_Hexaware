accounts = {'1': 1025452, '2': 13544, '3': 10254}

def check_account_balance():
    while True:
        account_number = input("Enter your account number: ")
        if account_number.isdigit() and len(account_number) > 1:
            if account_number in accounts:
                print("The account balance is: ", accounts[account_number])
                break
            else:
                print("Invalid account number. Please try again.")
        else:
            print("Invalid account number format. Please enter a 9-digit number.")

check_account_balance()