#The project entails creating the tic tac toe game.
#the below creates the spaces needed for the board
board = [' ' for x in range(9)]

#Function to display the board on the screen
def display():

  print(f'|{board[0]}||{board[1]}||{board[2]}|')
  print(f'|{board[3]}||{board[4]}||{board[5]}|')
  print(f'|{board[6]}||{board[7]}||{board[8]}|')

#Function to determine which player makes the move.
def move(icon):
  print()
  if icon == 'X':
    print('It is your turn player 1')
    print()
  else:
    print('It is your turn player 2')
    print()

#Get user input
  user = int(input('Enter a digit 1-9: '))
  if user >=1 and user <=9:

    if board[user-1] == ' ':
      board[user-1] = icon 
    else:
      print('That move is not available')
  else:
    print('Put a number between 1-9')

#Function to check who worn.
def win(icon):
  if(board[0]==icon and board[1]==icon and board[2]==icon)or\
    (board[3]==icon and board[4]==icon and board[5]==icon)or\
    (board[6]==icon and board[7]==icon and board[8]==icon)or\
    (board[0]==icon and board[3]==icon and board[6]==icon)or\
    (board[1]==icon and board[4]==icon and board[7]==icon)or\
    (board[2]==icon and board[5]==icon and board[8]==icon)or\
    (board[0]==icon and board[4]==icon and board[8]==icon)or\
    (board[2]==icon and board[4]==icon and board[6]==icon):
     return True
  else:
    return False

#Function to check if it is a draw

def draw():

  if ' ' not in board:
    return True
  else:
    return False

#Loop to keep the game running      
while True:

  display()
  move('X')
  display()
  if win('X'):
    print('Player 1 wins!')
    break
  elif draw():
    print('issa draw!')
    break
  move('O')
  if win('O'):
      display()
      print('Player 2 wins!')
      break
  elif draw():
    print('issa draw!')
    break

  print()




