print("==== Personal Finance Tracker ====")

income = 0
expenses = 0
balance = 0
expenses_categories = []

def add_income():
    global income, balance
    amount = int(input("Enter income: "))
    
    income += amount
    balance += amount

def add_expense():
    global expenses, balance
    
    amount = int(input("Enter expense amount: "))
    category = input("Enter expense type (food, travel, etc): ")
    
    expenses += amount
    balance -= amount
    expenses_categories.append((category, amount))

def show_summary():
    print("Income | Expenses | Balance")
    print(f"{income}     {expenses}     {balance}")

def show_expesse_list():
    print("Expense List:")
    print("Type  : amount ")
    for category, amount in expenses_categories:
        print(f"{category}: {amount}")

def menu():
    while True:
        print("\nTools:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Show Expenses")
        print("5. Exit")

        tool = int(input("Choose option: "))

        if tool == 1:
            add_income()
        elif tool == 2:
            add_expense()
        elif tool == 3:
            show_summary()
        elif tool == 4:
            show_expesse_list()
        elif tool == 5:
            break
        else:
            print("Invalid input!Try to input between 1-5")

menu()