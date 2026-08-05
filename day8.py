#DAY 8

#PYTHON CLASSES

#OOP - Object Oriented Programming.

#Class - A blueprint for creating objects
 
#PHONE 
  #has a battery, brand, RAM, storage - ATTRIBUTES(characteristics)

  #can call, charge, take a video, play music - METHODS(actions)

#FACEBOOK
#users have name, email, password, age

#users can log in, log out , post

#JOB
#name = JOBS
#email = jobs1234@gmail.com

#JOLE
#name = breakpoint

#TOYOTA
#wheels, doors, engine, seats - design
#class
#each car is an object

#class Students:
    #pass

#class tells python that you are creating a class
#Students is the class name
#: starts the class body
#pass it tells python that you are not adding anything

#OBJECT
#student1 = student()

#student1 stores an object in avariable
#student() creates a new student

#THE CONSTRUCTOR
#__init__()

#class Student:
    #def __init__(self,name,course):
        ##self.course = course

#SELF
#self allows each object to keep it's own data

#student1 = Student("BRITNEY","CYBER SECURITY")

#python thinks like
#self.name = "BRITNEY"


#ATTRIBUTES
#variables inside an object

#ACCESSING ATTRIBUTES
#print(self.name)

#METHODS
#functions inside classes



class Student:

    def __init__(self,name,course):

        self.name = name
        self.course = course

    def introduce(self):
        pass

        print(f"My name is {self.name}")
        print(f"I study {self.course}")

student1 = Student("JOHN","IT")
student2 = Student("BRITNEY","CYBER SECURITY")
student3 = Student("JOB","COMPUTER SCIENCE")
student4 = Student("MERCY","SOFTWARE ENGINEERING")
student5 = Student("ALEX","DATA SCIENCE")

student1.introduce()
student2.introduce()
student3.introduce()
student4.introduce()
student5.introduce()

#class tells python that you are basically creating a class
#Student name of the class
#colon starts the class body   Mlango...door


#object
#student1 = student()


#constructor
#self