#This is a bank simulator project using classes and objects

class Bank:

 #setting a default balance
  def __init__(self,name,pin,balance=500):

    self.name = name
    self.pin = pin
    self.balance = 500

#method to deposit money
  def deposit(self,amount):

    self.balance += amount
    print(f'Your new balance is {self.balance}')

 #method to withdraw money 
  def withdraw(self,amount):

    if self.balance >= amount:
      self.balance -= amount
      print(f'{amount} Has been withdrawn, Your new balance is {self.balance}')
    else:
      print('Insufficient balance')

 #method to display default balance 
  def statement(self):
    print(f'Welcome {self.name},your current balance is {self.balance}')
  
print('Welcome to Ashton Bank! Provide your details below: ')
print()
#get user input
name = input('Enter Account Name: ')
pin = input('Enter pin: ')

#create a savings account object and pass in user input
savings= Bank(name,pin)
#display balance
savings.statement()
print()

#loop to simulate deposit and withdrawal of money
choice = input('Do you want to deposit or withdraw or quit?: ').lower()

while choice != 'quit':

  if choice =='deposit':

    amount = int(input('Enter amount: '))
    savings.deposit(amount)

  elif choice =='withdraw':

    amount = int(input('Enter amount: '))
    savings.withdraw(amount)

  choice = input('Do you want to deposit or withdraw or quit?: ').lower()

