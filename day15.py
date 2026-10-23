#RECURSION
# A recursive function is a function that calls itself until it reaches a base case. It is a powerful tool in programming that allows for elegant solutions to problems that can be broken down into smaller, similar subproblems.

def countdown(n):
    if n == 0:
        return

    print(n)

    countdown(n - 2)

countdown(6)  

def hello(times):
    if times == 0:
        return

    print("Hello")

    hello(times - 1)

hello(5)

def countdown(n):
    print(n)
    countdown(n - 1)

    
