from database import load_data, save_data


# ===============================
# ADD ACCOUNT
# ===============================
def add_account():
    data = load_data()

    print("\n=== Add New Account ===")

    web_name = input("Enter website name: ").strip()
    user_name = input("Enter user name: ").strip()
    password = input("Enter password: ").strip()

    details = {
        "web_name": web_name,
        "user_name": user_name,
        "password": password
    }

    data.append(details)
    save_data(data)

    print("✔ Account saved successfully!\n")


# ===============================
# VIEW ACCOUNTS
# ===============================
def view_accounts():
    data = load_data()

    if not data:
        print("\n⚠ No accounts saved!\n")
        return

    print("\n=== Saved Accounts ===")

    for index, details in enumerate(data, start=1):
        print(f"\n[{index}] Website : {details['web_name']}")
        print(f"    Username: {details['user_name']}")
        print(f"    Password: {details['password']}")

    print()


# ===============================
# SEARCH ACCOUNT
# ===============================
def search_account():
    data = load_data()

    if not data:
        print("\n⚠ No accounts saved!\n")
        return

    se = input("\nEnter website name to search: ").strip()

    for details in data:
        if details["web_name"].lower() == se.lower():

            print("\n✔ Account Found")
            print(f"Website : {details['web_name']}")
            print(f"Username: {details['user_name']}")
            print(f"Password: {details['password']}\n")

            return

    print("✘ Website not found!\n")


# ===============================
# DELETE ACCOUNT
# ===============================
def delete_account():
    data = load_data()

    if not data:
        print("\n⚠ No accounts to delete!\n")
        return

    view_accounts()

    try:
        ch = int(input("Enter index to delete: "))
        python_index = ch - 1

        if python_index < 0 or python_index >= len(data):
            print("✘ Invalid index!\n")
            return

    except ValueError:
        print("✘ Please enter a valid number!\n")
        return

    removed = data.pop(python_index)
    save_data(data)

    print(f"✔ '{removed['web_name']}' removed successfully!\n")


# ===============================
# UPDATE ACCOUNT
# ===============================
def update_account():
    data = load_data()

    if not data:
        print("\n⚠ No accounts to update!\n")
        return

    view_accounts()

    try:
        op = int(input("Enter index to update: "))
        python_index = op - 1

        if python_index < 0 or python_index >= len(data):
            print("✘ Invalid index!\n")
            return

    except ValueError:
        print("✘ Please enter a valid number!\n")
        return

    print("\nEnter new details:")

    new_web = input("New website: ").strip()
    new_user = input("New username: ").strip()
    new_pass = input("New password: ").strip()

    # FIX: update dictionary, not replace it
    data[python_index]["web_name"] = new_web
    data[python_index]["user_name"] = new_user
    data[python_index]["password"] = new_pass

    save_data(data)

    print("✔ Account updated successfully!\n")