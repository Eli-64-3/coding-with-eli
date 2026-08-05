#INHERITANCE
#A class can inherit the properties and methods of other classes

class Dog:
    def __init__(self, sound):
        self.sound = sound

        print("Bark")

class Cat:
    def __init__(self,sound):
        self.sound = sound

        print("Meow")



#PARENT CLASS
#It's the original class
#contains the shared features

class Animal:
    def eat(self):
        print("IS Eating...")

#CHILD CLASS

class Dog(Animal):
    pass

#METHOD OVERRIDING
class Animal:
    def speak(self):
        print("SOUND :")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Wooffff!!!!")

dog = Dog()
dog.speak()

#SUPER()
#means "go to my parent class"

#CONSTRUCTOR INHERITANCE
#__init__

class Animal:
    def __init__(self,name):
        self.name = name
       
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)



dog = Dog("Bruno")
print(dog.name)