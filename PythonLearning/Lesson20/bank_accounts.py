class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"Account '{self.name}' created.")
        print(f"Balance = ${self.balance:.2f}\n")

    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}\n")
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}\n")

    def transfer(self, amount, account):
        try:
            print("*********")
            print("Transfer beginning... 🚀\n")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer complete! ✅")
            print("*********\n")
        except BalanceException as error:
            print("Transfer interrupted. ❌")
            print(error)
            print("*********\n")

class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit complete.")
        self.getBalance()

class SavingsAccount(InterestRewardAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print("Withdraw interrupted. ")
            print(error)