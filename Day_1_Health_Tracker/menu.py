from Day_1_Health_Tracker import measurements, view_data, delete_data,search_data,update_data
from summary import transformation,get_best_month

def main():

    while True:

        print("""
==== Health Tracker ====

1. Add Measurement
2. View Measurements
3. Delete data
4. Search Data
5. Update Data                            
6. Forecast Transformation
7. Best Month
8. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            measurements()

        elif choice == "2":
           view_data()

        elif choice == "3":
            delete_data()

        elif choice == "4":
            search_data()
        elif choice=="5":
            update_data()
        elif choice=="6":
            transformation()
        elif choice=="7":
            get_best_month()
        elif choice=="8":
            break
        else:
            print("Invalid choice")

main()