#FUNCTION ARGUMENTS & SCOPE
#We learn how to make our function much smarter

def order_pizza(size, toppings):
    print(f"{size} pizza with {toppings}.")

order_pizza("large", "pepperoni and mushrooms")

#1. POSITIONAL ARGUMENTS
#They depend on the order.

def student(name, age):
    print(name, age)

student("John", 20) #John 20

#2. KEYWORD ARGUMENTS
#Let's us specify which value belongs to which parameter.

student(age=21, name="Alice") #John 20


#3. DEFAULT ARGUMENTS

def pay(amount, currency="Kshs"):
    print(f"Paying {amount} in {currency}")

pay(500)

#custom currency
pay(500, "USD")


#SCOPE
#Scope ,eans the region of a program where a variable is accessible. There are two types of scope: global and local.

##Local Scope.
def test():
    x = 10 #local variable
    print(x)

test()

#Global Scope
school = "Machakos School"

def print_school():
    print(school)

print_school()


def calculated_area(length, width):
    area = length * width #local variable
    return area

print(calculated_area(10, 5))