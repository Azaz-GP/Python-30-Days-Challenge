# ===============================
# Shopping List Manager (TXT)
# ===============================


# ---------- ADD ITEM ----------
def add_item():
    item_name = input("Enter item name: ").strip()
    item_quantity = input("Enter item quantity: ").strip()

    if not item_name or not item_quantity:
        print("Item name and quantity cannot be empty!")
        return

    with open("shop.txt", "a") as file:
        file.write(f"{item_name},{item_quantity}\n")

    print("Item added successfully.")


# ---------- VIEW ITEMS ----------
def view_item():
    try:
        with open("shop.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Shopping list file not found.")
        return

    if not lines:
        print("Shopping list is empty!")
        return

    print("\n--- Shopping List ---")
    for index, line in enumerate(lines, start=1):
        line = line.strip()
        if "," in line:
            item_name, item_quantity = line.split(",")
            print(f"{index}. {item_name} - {item_quantity}")

    print("----------------------")


# ---------- REMOVE ITEM ----------
def remove_item():
    try:
        with open("shop.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Shopping list file not found.")
        return

    if not lines:
        print("Shopping list is empty!")
        return

    print("\nSelect item to remove:")
    for index, line in enumerate(lines, start=1):
        item_name, item_quantity = line.strip().split(",")
        print(f"{index}. {item_name} - {item_quantity}")

    try:
        user_num = int(input("Enter item number: "))
        index = user_num - 1

        if index < 0 or index >= len(lines):
            print("Invalid selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    lines.pop(index)

    with open("shop.txt", "w") as file:
        file.writelines(lines)

    print("Item removed successfully.")


# ---------- UPDATE ITEM ----------
def update_item():
    try:
        with open("shop.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Shopping list file not found.")
        return

    if not lines:
        print("Shopping list is empty!")
        return

    print("\nSelect item to update:")
    for index, line in enumerate(lines, start=1):
        item_name, item_quantity = line.strip().split(",")
        print(f"{index}. {item_name} - {item_quantity}")

    try:
        user_num = int(input("Enter item number: "))
        index = user_num - 1

        if index < 0 or index >= len(lines):
            print("Invalid selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    new_name = input("Enter new item name: ").strip()
    new_quantity = input("Enter new item quantity: ").strip()

    if not new_name or not new_quantity:
        print("Item name and quantity cannot be empty!")
        return

    lines[index] = f"{new_name},{new_quantity}\n"

    with open("shop.txt", "w") as file:
        file.writelines(lines)

    print("Item updated successfully.")


# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n===== Shopping List Manager =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select 1-5.")


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    main()