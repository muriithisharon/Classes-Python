import datetime
class Transaction:
    def __init__(self, date, time, narration, amount,transaction_type):
        self.transaction_type = transaction_type
        self.date = date
        self.time = time
        self.narration = narration
        self.amount = amount

class Account:
    def __init__(self, name,acc):
        self.name = name
        self._balance = 500
        self._account_number = acc
        self.loan_balance = 0
        self.deposits = []
        self.withdrawals = []
        self.minimum_balance = 500
        self.is_frozen = False
        self.transactions =[]
        

    #Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amount
    def deposit(self, amount):
        current_date = datetime.datetime.now()
        if amount > 0:
            self._balance += amount
            self.deposits.append(amount)
            self.transactions.append(Transaction(current_date, current_date.time(), "Deposit", amount, "Deposit"))
            return f"Dear {self.name}, your have deposited {amount} and your new balance is {self._balance}."
        
    # Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            current_date = datetime.datetime.now()
            self._balance -= amount
            self.withdrawals.append(amount)
            self.transactions.append(Transaction(current_date, current_date.time(), "Withdrawal", amount, "Withdrawal"))
            return f" Dear  {self.name}, your withdrawal of {amount} was successful and your balance is {self._balance}."
        return f"Dear {self.name} you have insufficient funds to withdraw {amount}. Your current balance is {self._balance}."
    
    def get_balance_value(self):
        return sum(t.amount for t in self.transactions if t.transaction_type == "Deposit") - sum(t.amount for t in self.transactions if t.transaction_type == "Withdrawal")
    def get_balance(self):
        balance = self.get_balance_value()
        return f"Hello {self.name}, your current  balance is {balance}."  
    # Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer(self, amount, target_account):
        if amount <= 0:
            return "Transfer amount must be positive"
        if self.is_frozen:
            return "Your account is frozen. Cannot transfer funds."
        if self.get_balance_value() < amount:
            return "Insufficient funds for transfer"
        if self.withdraw(amount):
            target_account.deposit(amount)
            self.transactions.append(Transaction(datetime.datetime.now(), datetime.datetime.now().time(), "Transfer", amount, "Transfer"))
            target_account.transactions.append(Transaction(datetime.datetime.now(), datetime.datetime.now().time(), "Transfer", amount, "Transfer"))
            return f'{self.name} you have transferred {amount} to {target_account.name}.'
        if self.withdraw(amount):
            target_account.deposit(amount)
            return f'{self.name} you have transferred {amount} to {target_account.name}.'
        return "Transfer failed"
    
    # Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def calculate_balance(self):
        total_deposits = sum(self.deposits)
        total_withdrawals = sum(self.withdrawals)
        self.balance = total_deposits - total_withdrawals
        return f"Hello {self.name}, your balance is {self.balance}."
    
    # Request Loan: Method to request a loan amount.
    def loan(self, amount):
        if amount > 0:
            self.balance += amount
            return f"You have received a loan of {amount}. Your new balance is {self.balance}."
        return "Loan request failed"
    
   # Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"You have repaid {amount} of your loan. Your new balance is {self.balance}."
        return "Repayment failed"
    
    def get_loan_balance(self):
        return f"Hello {self.name}, your loan balance is {self.balance}."
    # View Account Details: Method to display the account owner's details and current balance.
    def view_account_details(self):
        return f" Dear {self.name} - Account Number: {self.account_number}, Balance: {self.balance}, Deposits: {self.deposits}, Withdrawals: {self.withdrawals}"
    
    # Change Account Owner: Method to update the account owner's name.
    def change_account_name(self, new_name):
        if not new_name:
            raise ValueError("New name cannot be empty")
        self.name = new_name
        return f"Account name changed to {self.name}."
    
    # Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
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
    
    # Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def interest_calculation(self, rate):
        rate = 5 // 100
        interest = self.balance * rate
        self.balance += interest
        return f"Interest of {interest} added. New balance is {self.balance}."
    
    # Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.is_frozen = True
        return f"Account {self.account_number} is now frozen."
    def unfreeze_account(self):
        self.is_frozen = False
        return f"Account {self.account_number} is now unfrozen."
    
    # Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount.Close Account: Method to close the account and set all balances to zero and empty all transactions.
    def set_minimum_balance(self, amount):
        if amount < 1000:
            raise ValueError("Minimum balance cannot be less than 1000")
        self.minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}."
    def close_account(self):
        if self.balance == 0:
            return f"Account {self.account_number} closed successfully."
        

