import random

secret_number = random.randint(1,100)
attempts = 0

print("==== GAME HUB ====")

print("I have chosen a random between 1 and 100 go on and take a guess. ")

while True:
     guess = int(input("Enter your number: "))

     attempts += 1

     if guess < secret_number:
          print("Too Low. Try again. ")

     elif guess > secret_number:
          print("Too High. Try again. ")

     else:
          print("\n Congratulations!!!")
          print(f"The number was {secret_number}")
          print(f"You made {attempts} attempts.")
          break
     