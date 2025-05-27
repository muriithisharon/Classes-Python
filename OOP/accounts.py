class Account:
    def __init__(self, name,acc ):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.account_number = acc
        self.loan_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self.balance += amount
            return f"Hello {self.name}, your balance is {self.balance}."
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f" Hello {self.name}, your balance is {self.balance}."
        return "Insufficient funds"
    def get_balance(self):
        return f"Hello your balance is {self.balance}."
    
    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return f'{self.name} you have transferred {amount} to {target_account.name}.'
        return "Transfer failed"
    
    def loan(self, amount):
        if amount > 0:
            self.balance += amount
            return f"You have received a loan of {amount}. Your new balance is {self.balance}."
        return "Loan request failed"
   
    def repay_loan(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"You have repaid {amount} of your loan. Your new balance is {self.balance}."
        return "Repayment failed"
    def get_loan_balance(self):
        return f"Hello {self.name}, your loan balance is {self.balance}."
    def view_account_details(self):
        return f" Dear {self.name} - Account Number: {self.account_number}, Balance: {self.balance}, Deposits: {self.deposits}, Withdrawals: {self.withdrawals}"
    def change_account_name(self, new_name):
        if not new_name:
            raise ValueError("New name cannot be empty")
        self.name = new_name
        return f"Account name changed to {self.name}."
    def account_statement(self):
        statement = f"Account Statement for {self.name} Account No:{self.account_number}"
        statement += "Deposits"
        for deposit in self.deposits:
            statement += f" +{deposit}"
        statement += "Withdrawals"
        for withdrawal in self.withdrawals:
            statement += f"+{withdrawal}"
        statement += f"Current Balance: {self.balance}"
        return statement
    def interest_calculation(self, rate):
        rate = 5 // 100
        interest = self.balance * rate
        self.balance += interest
        return f"Interest of {interest} added. New balance is {self.balance}."
    def freeze_account(self):
        self.is_frozen = True
        return f"Account {self.account_number} is now frozen."
    def unfreeze_account(self):
        self.is_frozen = False
        return f"Account {self.account_number} is now unfrozen."
    def set_minimum_balance(self, amount):
        if amount < 1000:
            raise ValueError("Minimum balance cannot be less than 1000")
        self.minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}."
    def close_account(self):
        if self.balance == 0:
            return f"Account {self.account_number} closed successfully."