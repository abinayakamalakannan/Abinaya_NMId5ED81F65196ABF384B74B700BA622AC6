ns.
Filter changed files
 24 changes: 24 additions & 0 deletions24  
challenge 1.1.py
@@ -0,0 +1,24 @@
# 1.1 Implement a recursive function to calculate the factorial of a given number.

"""
1! = 1 x 1
2! = 2 x 1! --->2 x 1
3! = 3 x 2! --->3 x 2 x 1
.
.
10! = 10 x 9! ---> 10 x 9 x 8 x... x 1
Formula - n x (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number = int(input("Enter a value : "))
res = fact_rec(number)

print("The factorial of {} is {}.".format(number,res))
 21 changes: 21 additions & 0 deletions21  
challenge 1.2.py
@@ -0,0 +1,21 @@
# Leap year

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0
"""
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("Enter a year : "))

if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))

 43 changes: 43 additions & 0 deletions43  
challenge 2.1.py
@@ -0,0 +1,43 @@
'''Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance. Include methods to
deposit money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      # self.__account_balance = self.__account_balance+amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                                     self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      # self.__account_balance = self.__account_balance - amount
      print("Withdrew ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))
# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="Hari Prabu",
                      initial_balance=5000.0)
# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()
