class Account:
    def __init__(self):
        self.__bank="state bank"
        self.__username="Ajay"
        self.__password="Ajay.25sep"
        self.__branch="perungalathur branch"
        self.__mobilenumber="7418982509"
        self.__balance = 0

    def getname(self):
        print(self.__bank)
        print(self.__username)
        print(self.__password)
        print(self.__branch)
        print(self.__mobilenumber)

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
            print("current balance:",self.__balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("withdrawal successful.")
            print("current Balance:",self.__balance)

    def check_balance(self):
        print("Available balance:", self.__balance)

ob=Account()
ob.getname()
ob.deposit(10000)
ob.withdraw(5000)
ob.check_balance()   