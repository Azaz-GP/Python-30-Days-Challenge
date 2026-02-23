print("===== Personal Notes Saver =====")

def add_note():
    note = input("Enter Note: ")
    with open("notes.txt","a") as f:
        f.write(f"-> {note}\n")

def view_notes():
    while True:
     try:
        with open("notes.txt","r") as f:
            print(f.read())
            break
     except FileNotFoundError:
        print("No notes found yet.")

def menu():
    print("====== What you want to do =====")

    while True:
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Exit")

        try:
            ch = int(input("Enter choice: "))
            
        except ValueError:
            print("Enter a valid number!")
            continue

        if ch == 1:
            add_note()

        elif ch == 2:
            view_notes()

        elif ch == 3:
            print("Goodbye")
            break

        else:
            print("Invalid choice!")

menu()