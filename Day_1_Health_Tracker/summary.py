from database import(data_load,data_save)
def transformation():

    print("\n--- 4 Week Transformation Forecast ---")

    data = data_load()

    if not data:
        print("No data found!")
        return

    month = input("Enter month to forecast: ")

    found = False

    for details in data:

        if details["month"].lower() == month.lower():

            waist = details["waist"]
            workout = details["workout"]
            steps = details["steps"]

            initial_waist = waist

            print(f"\nForecast for {month}:")

            for week in range(1, 5):

                if steps >= 10000 and workout >= 4:
                    waist -= 0.25
                    status = "Extreme Burn"

                elif steps >= 7000 or workout >= 3:
                    waist -= 0.15
                    status = "Steady Progress"

                else:
                    waist -= 0.05
                    status = "Minimal Change"

                print(f"Week {week}: {status} | Waist: {waist:.2f}\"")

            print("\nResult:")
            print(f"Initial Waist: {initial_waist}")
            print(f"Final Waist: {waist:.2f}")
            print(f"Total Loss: {initial_waist - waist:.2f}\"")

            found = True
            break

    if not found:
        print("Month not found!")
def get_best_month():
    data=data_load()
    if not data:
        print("No measuments recored!")
        return
    best_month=data[0]
    for details in data:
       if details["waist"] < best_month["waist"]:
            best_month=details
    print("\n=== Best Month ===")
    print(f"Month   : {best_month['month']}")
    print(f"Waist   : {best_month['waist']}")
    print(f"Workout : {best_month['workout']}")
    print(f"Steps   : {best_month['steps']}\n")
def avg_steps():
    data=data_load()
    if not data:
        print("No measuments recored!")
        return
    total_steps=0
    total_steps = sum(details["steps"] for details in data)
    avg = total_steps / len(data)
    print(f"Average Steps: {avg:.2f}\n")

