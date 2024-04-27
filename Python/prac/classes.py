# Write code below 💖

class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.pin = pin
    self.balance = balance

  def deposit(self):
    self.balance += int(input("Enter money to add: "))
  
  def withdraw(self):
    self.balance -= int(input("Enter money to withdraw: "))

  def display_balance(self):
    print(f"You current balance is {self.balance}")

alex = BankAccount("Alexander","Aranes",6585,"Payroll",1234,1000)

alex.display_balance()
alex.deposit()
alex.display_balance()
alex.withdraw()
alex.display_balance()