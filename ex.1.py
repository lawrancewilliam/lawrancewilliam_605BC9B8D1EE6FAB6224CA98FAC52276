class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdraw Rs.{amount:.2f}. New balance: Rs.{self.__account_balance:.2f}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name}: Rs.{self.__account_balance:.2f}")



account1 = BankAccount("12345", "william", 2000.0)


account1.display_balance()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()
