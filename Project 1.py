#Health portion for a video game

#Depending on the difficulty the program determines how much portion is going to be added to the initial health portion.

#import random to generate a random number to use.
import random;

#initial health portion
health = 50

#check for difficulty to determine how much portion to be added.
#ranges from 1 to 3 being the hardest level.

difficulty = 3

#generate a random integer and divide it with the level of difficulty.

result = int(random.randint(25,50)/difficulty)

#print out the result

print(f'You were added a portion of {result} and now your total  is {health + result}')
