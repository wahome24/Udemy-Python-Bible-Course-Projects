#The program is a cinema simulator that shows a list of available movies and only allows a user to watch a movie depending on the age rating and seats available.

#list of movies available
movies = {"Deadpool":{'age rating':18,'seats left':2},
          'Trolls':{'age rating':12,'seats left':3}

}
#Displaying available movies to the user
print('Welcome to Cinema, we are currently showing the below movies!')
print()
for item in movies.keys():
   print(item)

print()
#Getting user input
choice = input('Which movie do you want to watch ? ').capitalize()

while choice != 'Stop':
 #checking if the movie is in the list   
  if choice in movies:
      age = int(input('Kindly enter your age : '))
      seatsleft = movies[choice]['seats left']
      if age >=movies[choice]['age rating']: #checking age of the user
        if seatsleft > 0: #checking if there are seats available
          print('Enjoy the movie')
          movies[choice]['seats left']-=1
          #print(f'Tickets left: {seatsleft}')
        if seatsleft <=0:
          print(f'Sorry, we are out of {choice} tickets! Try a different movie.')
      
      else:
          print('You do not meet the age limit, choose another movie')

  else:
    print('This movie is not currently showing!')

  choice = input('Which movie do you want to watch ? ').capitalize()


