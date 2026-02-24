import income
import expense
import summary

def menu():
    while True:
        print("\n===== Smart Expense Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Expenses")
        print("4. Show Summary")
        print("5. Exit")
        while True:
            try:
             choice = int(input("Choose option: "))
             break
            except:
                print("only numbers")

        if choice == 1:
            income.add_income()

        elif choice == 2:
            expense.add_expense()

        elif choice == 3:
            expense.show_expenses()

        elif choice == 4:
            summary.show_summary()

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

menu()