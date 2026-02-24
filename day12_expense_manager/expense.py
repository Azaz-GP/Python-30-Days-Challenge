import storage

def add_expense():
    while True:
        try:
         amount = int(input("Enter expense amount: "))
         break
        except ValueError:
            print("only integers")
    category = input("Enter category (food, travel, etc): ")

    storage.total_expense += amount
    storage.expenses_list.append((category, amount))

    print("Expense added successfully!")

def show_expenses():
    if not storage.expenses_list:
        print("No expenses recorded.")
        return

    print("----- Expense List -----")
    for cat, amt in storage.expenses_list:
        print(f"{cat} : {amt}")

def get_total_expense():
    return storage.total_expense