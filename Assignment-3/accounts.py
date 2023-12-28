class Account:
    def __init__(self, acc_number='', acc_type='', acc_balance=0.0):
        self.__account_number = acc_number
        self.__account_type = acc_type
        self.__account_balance = acc_balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_account_balance(self):
        return self.__account_balance

    # Setter methods
    def set_account_number(self, acc_number):
        self.__account_number = acc_number

    def set_account_type(self, acc_type):
        self.__account_type = acc_type

    def set_account_balance(self, acc_balance):
        self.__account_balance = acc_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. Updated balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. Updated balance: ${self.__account_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def calculate_interest(self):
        interest_rate = 4.5  
        interest_amount = (self.__account_balance * interest_rate) / 100
        return interest_amount

    def print_account_info(self):
        print("Account Information:")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Account Balance: ${self.__account_balance}")


account1 = Account('123456', 'Savings', 1000.0)

account1.print_account_info()

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)  

# Calculating interest
interest = account1.calculate_interest()
print(f"Interest Amount: ${interest}")
