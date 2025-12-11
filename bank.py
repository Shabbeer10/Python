from abc import ABC, abstractmethod  # For abstraction

# Encapsulation: Using private variables and getters/setters
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number  # Private variable
        self.__account_holder = account_holder
        self.__balance = balance

    # Getter for account balance
    def get_balance(self):
        return self.__balance

    # Setter for deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Setter for withdrawal
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

# Abstraction: Abstract class for account types
class Loan(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Inheritance: Specialized account types inherit from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest for Savings Account: {interest}")
        return interest

class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Overriding withdraw to include overdraft limit
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            if amount > self.get_balance():
                overdraft_used = amount - self.get_balance()
                print(f"Using overdraft of {overdraft_used}")
            self._Account__balance -= amount  # Accessing private variable from base class
            print(f"Withdrew {amount}. New balance is {self._Account__balance}")
        else:
            print("Exceeds overdraft limit or invalid amount.")

# Polymorphism: A function that works with any account type
def display_account_details(account):
    print("Account Details:")
    print(f"Balance: {account.get_balance()}")
    account.deposit(1000)  # Adding a deposit
    account.withdraw(500)  # Withdrawing some amount

# Example usage:
if __name__ == "__main__":
    # Create instances
    savings = SavingsAccount("SA123", "John Doe", 5000, 0.03)
    current = CurrentAccount("CA456", "Jane Smith", 2000, 1000)

    # Encapsulation
    print("\nSavings Account:")
    display_account_details(savings)
    savings.calculate_interest()  # Abstraction

    print("\nCurrent Account:")
    display_account_details(current)

    # Polymorphism in action
    print("\nPolymorphism Example:")
    for account in [savings, current]:
        display_account_details(account)
j