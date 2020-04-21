#The program teaches on getting user input and string formatting.

#The program will combine user input into one string.

#Get user input:

name = input('Enter your name: ').capitalize()
print()
age = input('Enter your age: ')
print()
residence = input('Enter where you live: ').capitalize()
print()
#Joining everything together using string formating

output = print(f'My name is {name}, I am {age} years old and I live in {residence}')


#you can wrap the above into a while loop so the program can continue running indefinately

user = input('Enter start or stop: ').lower()
print() #use an empty print to create spacing.
while user != 'stop':

  if user =='start':
    name = input('Enter your name: ').capitalize()
    print()
    age = input('Enter your age: ')
    print()
    residence = input('Enter where you live: ').capitalize()
    print()
    output = print(f'My name is {name}, I am {age} years old and I live in {residence}')
  print()
  user = input('Enter start or stop: ').lower()
  print()
