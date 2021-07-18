class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else: 
            print("Error: Balance in the negative")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_checking = BankAccount(int_rate=0.01, balance=0)
        self.account_savings = BankAccount(int_rate=0.02, balance=500)
    
    def make_deposit(self, amount):
        self.account_checking.deposit(amount)
        self.account_savings.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account_checking.withdraw(amount)
        self.account_savings.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User: " + str(self.name) + ", Balance: $" + str(self.account_checking))
        print("User: " + str(self.name) + ", Balance: $" + str(self.account_savings))
        return self

ashley = User("Ashley", "ashley123@gmail.com")
ashley.account_savings.deposit(100).display_account_info()