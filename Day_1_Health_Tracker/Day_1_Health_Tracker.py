from database import data_load, data_save


def measurements():

    data = data_load()

    month = input("Enter month: ").strip()

    for details in data:
        if details["month"].lower() == month.lower():
            print("Month already exists!")
            return

    try:
        waist = float(input("Enter waist: "))
        workout = int(input("Enter workout days (0-7): "))
        steps = int(input("Enter steps (0-20000): "))

    except ValueError:
        print("Invalid input!")
        return

    new_data = {
        "month": month,
        "waist": waist,
        "workout": workout,
        "steps": steps
    }

    data.append(new_data)

    data_save(data)

    print("✔ Data saved successfully!\n")


def view_data():

    data = data_load()

    if not data:
        print("\n⚠ No measurements saved!\n")
        return

    print("\n=== Saved Measurements ===\n")

    for index, details in enumerate(data, start=1):

        print(f"""{index}.
Month   : {details['month']}
Waist   : {details['waist']}
Workout : {details['workout']}
Steps   : {details['steps']}
""")


def delete_data():

    data = data_load()

    if not data:
        print("\n⚠ No measurements saved!\n")
        return

    view_data()

    try:
        de = int(input("Enter index you want to delete: "))

        python_index = de - 1

        if python_index < 0 or python_index >= len(data):

            print("Invalid index")
            return

    except ValueError:

        print("Only numbers!")
        return

    data.pop(python_index)

    data_save(data)

    print("✔ Measurement removed!\n")


def search_data():

    data = data_load()

    if not data:
        print("\n⚠ No measurements saved!\n")
        return

    se = input("\nEnter month name to search: ").strip()

    for de in data:

        if de["month"].lower() == se.lower():

            print(f"""
Month   : {de['month']}
Waist   : {de['waist']}
Workout : {de['workout']}
Steps   : {de['steps']}
""")

            return

    print("✘ Month not found!\n")


def update_data():

    data = data_load()

    if not data:
        print("\n⚠ No measurements saved!\n")
        return

    view_data()

    try:
        op = int(input("Enter index to update: "))

        python_index = op - 1

        if python_index < 0 or python_index >= len(data):

            print("✘ Invalid index!\n")
            return

    except ValueError:

        print("✘ Please enter valid number!\n")
        return

    try:

        new_waist = float(input("Enter new waist: "))
        new_workout = int(input("Enter workout days: "))
        new_steps = int(input("Enter steps: "))

    except ValueError:

        print("Invalid input!")
        return

    data[python_index]["waist"] = new_waist
    data[python_index]["workout"] = new_workout
    data[python_index]["steps"] = new_steps

    data_save(data)

    print("✔ Measurement updated successfully!\n")