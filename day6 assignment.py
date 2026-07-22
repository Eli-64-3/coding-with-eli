# ATM
name = input("Enter your name: ")

password = input("Enter your password: ")

balance = int(input("Enter your balance: "))

if name == "eli" and password ==  "12345567789":

    print("Welcome to the ATM")

    print("Your balance is: " + str(balance))

if name != "eli" and password !=  "12345567789":

    print("Invalid name or password")
  