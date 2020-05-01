#The program comprises of two parts.

#Part1 - The program ask the user for their name and check if it is included in the database(list). If present it will ask the user if they want to be deleted. If yes, the user will be deleted.

#Part2 - if the user is not available the program will ask the user if they want to be added. If yes, the user will be added.

#list of initial available names
result= ['Erastus','wahome','Gacheru']

#get user name 

user = input('Enter your name: ').capitalize()

#while loop to make the program continue running.
while user != 'stop':

#asking the user if they want to be removed
  if user in result:
    print(f'Welcome {user}')
    print()
    remove= input('Would you like to be removed from the database? yes/no :').lower()

    if remove == 'yes':
      result.remove(user)
      print('You have been removed from record')
      print(result)#shows the initial list with the removed user
    else:
      print('Thank you for your confirmation, You are logged in.')
  else:
    print('That name is not in record')
    
    #adding the user if they do not exist.
    add = input('Would you like to be added to our records? yes/no: ').lower()

    if add == 'yes':
      result.append(user)
      print('Your record has been added proceed to login')
      print(result)
    else:
      print('Try again')
      
  user = input('Enter your name: ').capitalize()
