import storage

def add_income():
    while True:
        try:
         amount = int(input("Enter income amount: "))
         break
        except ValueError:
           print("Only Integers")
    storage.total_income += amount
    print("Income added successfully!")

def get_total_income():
    return storage.total_income