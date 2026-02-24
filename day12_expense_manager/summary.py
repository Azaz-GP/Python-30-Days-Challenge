import storage

def show_summary():
    balance = storage.total_income - storage.total_expense

    print("\n===== Financial Summary =====")
    print(f"Total Income   : {storage.total_income}")
    print(f"Total Expense  : {storage.total_expense}")
    print(f"Balance        : {balance}")