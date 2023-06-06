class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        print("Hello! Welcome to the deposite and withdrawal Machine")

    def deposit(self, amount):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        if not isinstance(amount, (int, float)):
            raise ValueError("invalid input use a digit number only")
        if amount <= 0:
            raise ValueError("Can only positive amount deposited")
        print("\n Amount deposited:", amount)


    def withdraw(self, amount):
        amount = float(input("Enter amount to be withdrawn: "))
        self.balance -= amount
        if not isinstance(amount, (int, float)):
            raise ValueError("invalid input use a digit number only")
        if amount <= 0:
            raise ValueError("Can only positive amount withdrawn")
        print("\n Amount withdrew: ", amount)

    def get_balance(self):
        return self.balance

    def display(self):
        print("\n Net Available balance = ", self.balance)

s = BankAccount(1000)

s.deposit(500)
s.withdraw(200)
s.display()

