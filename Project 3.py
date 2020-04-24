#The program asks a user for their email and returns a username and domain.
#the username is what is before the @ symbol and the domain is what comes after the symbol.
#This will be implemented through slices.

##Get user email
email = input('Enter your email address: ').strip()

#slice the username from the email
username = user[:user.index('@')]

#slice the domain from the email
domain= user[user.index('@')+1:]

#string formating
print(f'Hi there,your username is {username} and your domain is {domain}')

#you can also create a while loop o keep the program running.
