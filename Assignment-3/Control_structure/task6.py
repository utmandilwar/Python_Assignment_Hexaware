transaction_history = []

# Function to display transaction history
def display_transaction_history(history):
    if not history:
        print("No transactions recorded yet.")
    else:
        print("Transaction History:")
        for idx, transaction in enumerate(history, start=1):
            print(f"{idx}. {transaction}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a deposit")
    print("2. Add a withdrawal")
    print("3. Display transaction history")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        transaction_history.append(f"Deposit: +${amount}")
        print(f"Deposit of ${amount} added.")
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        transaction_history.append(f"Withdrawal: -${amount}")
        print(f"Withdrawal of ${amount} added.")
    elif choice == '3':
        display_transaction_history(transaction_history)
    elif choice == '4':
        print("Exiting program. Transaction history:")
        display_transaction_history(transaction_history)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
