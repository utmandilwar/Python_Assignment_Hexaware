def calculate_future_balance(initial_balance, annual_interest_rate, years):
    future_balance = initial_balance * (1 + annual_interest_rate/100)**years
    return future_balance

def calculate_future_balances():
    n = int(input("Enter the number of customers: "))

    for i in range(n):
        initial_balance = float(input("Enter the initial balance for customer " + str(i+1) + ": "))
        annual_interest_rate = float(input("Enter the annual interest rate for customer " + str(i+1) + ": "))
        years = int(input("Enter the number of years for customer " + str(i+1) + ": "))

        future_balance = calculate_future_balance(initial_balance, annual_interest_rate, years)
        print("The future balance for customer " + str(i+1) + " is: ", future_balance)

calculate_future_balances()