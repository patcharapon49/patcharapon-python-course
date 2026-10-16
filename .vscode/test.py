class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(f"Your balance is {self.__balance} Baht")

    def deposit(self, amount):
        if amount < 0:
            print("Please enter an amount greater than 0")
        elif amount > self.__balance:
            print("You can't deposit more than your balance")
        else:
            self.__balance += amount
            print(f"Your balance is {self.__balance} Baht")
class InterestFeature(BankAccount):
    def calculate_interest(rate):
        interest = BankAccount.self.balance * (rate / 100)
        print(f"Interest = {interest}")
        return interest