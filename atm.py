class ATM :
    def __init__(self,balance) :
        self.balance=balance
    def bal(self):
        self.balance=3

object=ATM("e")
object.bal()
amount=object.balance
print("Your Current Balance")
print(amount)
w1=int(input("How much would you like to add to your balance"))
print(amount+w1)
