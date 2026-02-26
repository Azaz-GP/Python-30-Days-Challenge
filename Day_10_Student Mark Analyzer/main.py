import student_mark_analyszer as m

def main():

    while True:

        # show menu every loop
        print("\n==== Student Marks Analyzer ====")
        print("1. New Student")
        print("2. View Data")
        print("3. Exit")

        # take input safely
        try:
            ch = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter number only.")
            continue

        # choice handling
        if ch == 1:
            m.add_student()

        elif ch == 2:
            m.view_data()

        elif ch == 3:
            print("Good bye")
            break

        else:
            print("Invalid choice")

# start program
main()