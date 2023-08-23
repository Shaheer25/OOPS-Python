class BankAccount:

    def __init__(self,balance,accountNumber):
        self.balance=balance
        self.accountNumber=accountNumber

    def deposite(self,amount):
        if amount > 0:
            self.balance+=amount

    def withdraw(self,ammount):
        if 0<ammount<=self.balance:
            self.balance -=ammount
        else :
            print("Insufficient Balance")

    def getbalance(self):
        return self.balance

account=BankAccount(1000,"123456")

print("balance",account.balance)

account.deposite(500)

print("Balance after Depo",account.getbalance())

account.withdraw(900)

print("Balance after Withdraw",account.getbalance())


