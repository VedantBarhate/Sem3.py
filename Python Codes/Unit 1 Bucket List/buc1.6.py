# Implement a class BankAccount with private attributes balance and account_number. Provide public methods to deposit and withdraw money, and to check the balance. Ensure that the balance cannot be set directly from outside the class.
# Concepts Covered: Encapsulation, Private Variables

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

my_account = BankAccount("12345", 1000)
my_account.deposit(500)
my_account.withdraw(200)

print(my_account.get_balance())