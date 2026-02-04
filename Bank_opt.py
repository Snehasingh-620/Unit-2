class bank:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = 1000

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}.")

my_account = bank("123456789", 0)
my_account.deposit(5000)
my_account.withdraw(500)

