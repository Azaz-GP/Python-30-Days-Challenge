print("===== Unique Visitor Tracker =====")

day1 = set()
day2 = set()


def add_day1():
    vid = int(input("Enter visitor ID for Day 1: "))
    day1.add(vid)


def add_day2():
    vid = int(input("Enter visitor ID for Day 2: "))
    day2.add(vid)


def show_total_unique():
    total = day1 | day2   # union
    print(f"Total unique visitors: {len(total)}")


def show_common():
    common = day1 & day2   # intersection
    print(f"Common visitors: {common}")
    print(f"Count: {len(common)}")


def menu():
    while True:
        print("\n1. Add Day 1 Visitor")
        print("2. Add Day 2 Visitor")
        print("3. Show Total Unique Visitors")
        print("4. Show Common Visitors")
        print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            add_day1()
        elif ch == 2:
            add_day2()
        elif ch == 3:
            show_total_unique()
        elif ch == 4:
            show_common()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid input")


menu()