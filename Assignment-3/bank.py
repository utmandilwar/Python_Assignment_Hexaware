from accounts import accounts

class Bank:
    def create_account(self, acc_number, acc_type, acc_balance):
            return accounts(acc_number, acc_type, acc_balance)

    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def calculate_interest(self, account):
        account.calculate_interest


class SavingsAccount(accounts):
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited ${amount}. Updated balance: ${self.get_balance()}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() >= amount:
                self.set_balance(self.get_balance() - amount)
                print(f"Withdrew ${amount}. Updated balance: ${self.get_balance()}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def calculate_interest(self):
        interest_rate = 4.5  # Fixed interest rate of 4.5% for savings accounts
        interest_amount = (self.get_balance() * interest_rate) / 100
        self.set_balance(self.get_balance() + interest_amount)
        print(f"Interest calculated and added. Updated balance: ${self.get_balance()}")


class CurrentAccount(accounts):
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited ${amount}. Updated balance: ${self.get_balance()}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew ${amount}. Updated balance: ${self.get_balance()}")
        else:
            print("Invalid withdrawal amount.")

    def calculate_interest(self):
        print("Interest calculation is not applicable for Current Accounts.")


class Bank:
    def create_account(self):
        print("Choose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            acc_balance = float(input("Enter initial balance: "))
            return SavingsAccount(acc_number, customer_name, acc_balance)
        elif choice == '2':
            acc_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            acc_balance = float(input("Enter initial balance: "))
            return CurrentAccount(acc_number, customer_name, acc_balance)
        else:
            print("Invalid choice. Creating default Savings Account.")
            return SavingsAccount()


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Calculate Interest")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account = bank.create_account()
            print("Account created.")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '4':
            account.calculate_interest()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
