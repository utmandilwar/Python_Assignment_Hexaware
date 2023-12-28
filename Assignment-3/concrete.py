from bankaccount import bankaccount

class SavingsAccount(bankaccount):
    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
    class CurrentAccount(bankaccount):
        def __init__(self, account_number, customer_name, balance):
            super().__init__(account_number, customer_name, balance)
            self.overdraft_limit = 500

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def calculate_interest(self):
        return 0