balance = 1000.0

def display_menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f"Your balance is: ${balance:.2f}")

def deposit_money(amount):
    global balance
    balance += amount
    print(f"Deposited: ${amount:.2f}")
    check_balance()

def withdraw_money(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrawn: ${amount:.2f}")
        check_balance()

while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit_money(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        withdraw_money(amount)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
