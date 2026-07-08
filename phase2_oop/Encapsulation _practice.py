"""class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark      # It's hidden system

    def get_mark(self):
       print(f"Name: {self.name}")    
       print(f"Mark: {self.__mark}")

s1 = Student("Injamam", 95)
s1.get_mark()           # Right way 
  """








class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private variable!

    def get_balance(self):
        print(f"{self.name}'s balance: {self.__balance} TK")

    # def deposit(self, amount):
    #     self.__balance += amount
    #     print(f"{amount} TK deposited successfully!")

    # def withdraw(self, amount):
    #     if amount > self.__balance:
    #         print("Insufficient balance!")
    #     else:
    #         self.__balance -= amount
    #         print(f"{amount} TK withdrawn successfully!")
name = input("Enter your Name : ")
blance = int(input("Enter your first blance :"))

acc = BankAccount(name, blance)

acc.get_balance()

# acc.deposit(500)
# acc.get_balance()
# acc.withdraw(2000)
# acc.withdraw(500)
# acc.get_balance()









"""class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # __ দিয়ে লুকানো হয়েছে!

    # balance দেখার উপায়
    def get_balance(self):
        print(f"{self.name} এর balance: {self.__balance} টাকা")

    # টাকা জমা
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} টাকা জমা হলো!")

    # টাকা তোলা
    def withdraw(self, amount):
        if amount > self.__balance:
            print("balance নেই!")
        else:
            self.__balance -= amount
            print(f"{amount} টাকা তোলা হলো!")


# Object তৈরি
acc = BankAccount("Injamam", 1000)

acc.get_balance()      # balance দেখো
acc.deposit(500)       # টাকা জমা
acc.get_balance()      # আবার দেখো
acc.withdraw(2000)     # বেশি তুলতে চাইলে
acc.withdraw(500)      # সঠিক পরিমাণ
acc.get_balance()      # শেষ balance"""