from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Rick = BankAccount(2000, "Rick")

# Dave.getBalance()
# Rick.getBalance()

# Dave.deposit(300)

# Dave.withdraw(10000)
# Dave.withdraw(100)

# Dave.transfer(10000, Rick)
# Dave.transfer(100, Rick)

# Dave.transfer(100, Rick)

Jim = InterestRewardAccount(100, "Jim")
# Jim.getBalance()
# Jim.deposit(100)
# Jim.transfer(100, Rick)

Mondy = SavingsAccount(1000, "Mondy")
Mondy.deposit(100)
# Mondy.transfer(10000, Jim)
Mondy.transfer(100, Jim)