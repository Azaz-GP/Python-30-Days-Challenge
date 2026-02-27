from manager import (
    add_account,
    view_accounts,
    search_account,
    delete_account,
    update_account
)


# ===============================
# MENU FUNCTION
# ===============================
def menu():
    while True:
        print("=================================")
        print("       PASSWORD MANAGER")
        print("=================================")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Update Account")
        print("6. Exit")
        print("=================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            search_account()

        elif choice == "4":
            delete_account()

        elif choice == "5":
            update_account()

        elif choice == "6":
            print("\nExiting Password Manager...")
            print("Goodbye!\n")
            break

        else:
            print("\nInvalid choice! Please select 1–6.\n")


# ===============================
# PROGRAM START
# ===============================
if __name__ == "__main__":
    menu()