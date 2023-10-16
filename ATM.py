class ATM:
    def __init__(self, balance, transaction_history=None):
        self.balance = balance
        self.transaction_history = transaction_history or []

    def display_balance(self):
        print(f"Your account balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f} successfully.")
        else:
            print("Invalid amount or insufficient balance for withdrawal.")

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount:.2f} to {recipient}")
            print(f"Transferred ${amount:.2f} to {recipient} successfully.")
        else:
            print("Invalid amount or insufficient balance for transfer.")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    account1 = ATM(1000)
    account2 = ATM(500)

    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Display Transaction History")
        print("6. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            account1.display_balance()
        elif choice == '2':
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter the transfer amount: "))
            account1.transfer(amount, account2)
        elif choice == '5':
            account1.display_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
