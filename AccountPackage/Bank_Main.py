from Bank import Bank


def main():
    bank = Bank()

    while True:
        print("\nOptions:")
        print("1. Register Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            pin = input("Enter your PIN: ")
            bank.register(first_name, last_name, pin)
            print("Account registered successfully.")

        elif choice == "2":
            account_number = input("Enter your account number: ")
            amount = int(input("Enter the deposit amount: "))
            bank.deposit(amount, account_number)
            print("Deposit successful.")

        elif choice == "3":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            amount = int(input("Enter the withdrawal amount: "))
            bank.withdraw(amount, account_number, pin)
            print("Withdrawal successful.")

        elif choice == "4":
            from_account_number = input("Enter your account number: ")
            from_pin = input("Enter your PIN: ")
            to_account_number = input("Enter the recipient's account number: ")
            to_pin = input("Enter the recipient's PIN: ")
            transfer_amount = int(input("Enter the transfer amount: "))
            bank.transfer(from_account_number, to_account_number, transfer_amount, from_pin, to_pin)
            print("Transfer successful.")

        elif choice == "5":
            account_number = input("Enter your account number: ")
            account = bank.find_account(account_number)
            print(f"Account Balance: {account.get_balance()}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

