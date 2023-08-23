class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance


# Creating an instance of the BankAccount class
account = BankAccount("123456", 1000)

# Accessing attributes through methods (encapsulation)
print("Initial balance:", account.get_balance())  # Output: Initial balance: 1000
account.deposit(500)
print("Balance after deposit:", account.get_balance())  # Output: Balance after deposit: 1500
account.withdraw(800)
print("Balance after withdrawal:", account.get_balance())  # Output: Balance after withdrawal: 700
