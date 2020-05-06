#This program tests on understanding of while loops.
#The program keeps running until the user enters the required words making the program to stop.

#Gives the user a random question to answer.
from random import choice

questions = ['why are there different races? ','What is your favorite travel destination? ']

question=choice(questions)

answer =input(question).capitalize()
print()
while answer != 'Don\'t know':

 #the program will ask why until the user enters Don't know.
  answer =input('Why ? :').capitalize()

print('Mmmmmh, Okay')
