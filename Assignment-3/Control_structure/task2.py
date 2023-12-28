from control_structure import task1;

def check_balance(current_balance):
    print("Your current balance is: ", current_balance)

def withdraw(current_balance, withdrawal_amount):
    if withdrawal_amount % 100 == 0 or withdrawal_amount % 500 == 0:
        if withdrawal_amount <= current_balance:
            current_balance -= withdrawal_amount
            print("You have successfully withdrawn: ", withdrawal_amount)
            print("Your new balance is: ", current_balance)
        else:
            print("Withdrawal amount exceeds your available balance.")
    else:
        print("Withdrawal amount must be a multiple of 100 or 500.")
    return current_balance

def deposit(current_balance, deposit_amount):
    current_balance += deposit_amount
    print("You have successfully deposited: ", deposit_amount)
    print("Your new balance is: ", current_balance)
    return current_balance

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        current_balance = int(input("Enter your current balance: "))
        check_balance(current_balance)
    elif option == 2:
        current_balance = int(input("Enter your current balance: "))
        withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
        current_balance = withdraw(current_balance, withdrawal_amount)
    elif option == 3:
        current_balance = int(input("Enter your current balance: "))
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        current_balance = deposit(current_balance, deposit_amount)
    elif option == 4:
        break
    else:
        print("Invalid option.")