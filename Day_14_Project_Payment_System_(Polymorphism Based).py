class PaymentMethod:
    def pay(self,amount):
        print(f"Processing payment of {amount}....")
class CreditCard(PaymentMethod):
    def pay(self, amount):
        super().pay(amount)
        print(f"Payment {amount} is done via CreditCard")
class DebitCard(PaymentMethod):
    def pay(self, amount):
         super().pay(amount)
         print(f"Payment {amount} is done via DebitCard")
class EasyPaisa(PaymentMethod):
    def pay(self, amount):
         super().pay(amount)
         print(f"Payment {amount} is done via EasyPaisa")
class JazzCash(PaymentMethod):
    def pay(self, amount):
         super().pay(amount)
         print(f"Payment {amount} is done via JazzCash")
payments=[CreditCard(),DebitCard(),EasyPaisa(),JazzCash()]
for acc in payments:
    acc.pay(3000)

