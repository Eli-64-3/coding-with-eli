#FUNCTIONS -- The secret to reusable code.


#A Fucnction is a re-usable block of code that performs a specific task.

def welcome():
    print("Welcome to the program!")

welcome()
welcome()

#FUNCTIONS WITH PARAMETERS
def greet(name):
    print(f"Hello {name}!")

greet("Alice")
greet("Job")
greet("Tom")


#Multiple Parameters

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

#calling the function
introduce("Alice", 25)
introduce("Betsy", 19)
introduce("John", 30)

#Return values from functions
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 10)

answer = add_numbers(5, 10)
print(answer)

#with return function
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)

#PRINT              VS           RETURN

#displays info on the screen      Sends info back to the caller
#Cannot be reused                 can be reused
#Used for output only             Used for output and further processing
#Is mainly for the user           mainly for the program

#I would love to visit {city} with {friend}