#The aim of this project is to showcase knowledge of classes and objects.
#We will create a class student with several students as objects.

#code for the class
class Student:

  def __init__(self,name,registration,course,year):

    self.name = name
    self.registration = registration
    self.course = course
    self.year = year

#methods  
  def enroll(self):

    registrations=[101,102,110,152,158]

    if self.registration in registrations:
      print(f'Welcome {self.name}')
    else:
      print(f'registration {self.registration} is not in our school records')

  def __str__(self):
    return 'This is a student object'

#getting user input 
name = input('Enter name: ')
reg =int(input('Enter your registration: '))
course= input('Enter your course:  ')
yos= int(input('Enter your year of study: '))

#passing user input to create the student object
student = Student(name,reg,course,yos)

#method to check if student is enrolled
student.enroll()



