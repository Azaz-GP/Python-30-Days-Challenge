class BankAccount:

    bank_name = "HBL Bank"
    total_accounts = 0
    account_numbers = set()

    def __init__(self, name, num):

        if num in BankAccount.account_numbers:
            raise ValueError("Account number already exists!")

        print("Account created!")

        self.account_holder_name = name
        self.account_number = num
        self.__balance = 0

        BankAccount.total_accounts += 1
        BankAccount.account_numbers.add(num)


    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")
            return False

        self.__balance += amount
        print(f"{amount} deposited successfully")
        return True


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdraw amount!")
            return False

        if amount > self.__balance:
            print("Insufficient balance!")
            return False

        self.__balance -= amount
        print(f"{amount} withdrawn successfully")
        return True


    def transfer(self, other_account, amount):

        if self is other_account:
            print("Cannot transfer to same account!")
            return

        if self.withdraw(amount):
            other_account.deposit(amount)
            print("Transfer successful")


    def get_balance(self):
        return self.__balance


    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


    @staticmethod
    def bank_info():
        print("This is a secure banking system")


    def __str__(self):

        return (
            f"Account Holder: {self.account_holder_name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: Rs {self.get_balance():,}\n"
            f"Bank: {type(self).bank_name}"
        )


    def __del__(self):
        print(f"Account of {self.account_holder_name} deleted")

BankAccount.bank_info()

s1 = BankAccount("Azaz", 101)
s2 = BankAccount("Ali", 102)

s1.deposit(5000)
s1.withdraw(2000)

print()
print(s1)

print()
print("Total accounts:", BankAccount.total_accounts)

BankAccount.change_bank_name("Meezan Bank")

print()
print(s1)
print(s2)
print()
s1.transfer(s2,1000)
print(s1)
print(s2)