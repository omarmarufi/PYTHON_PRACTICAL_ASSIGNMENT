#1- I have used the function def Fibonacci(number)
#2- Here, if (number == 1) check whether the given number is 1 or not.
#3- elif (number == 2) check whether the given number is 2 or not.
#4- function Fibonacci() is used to calculate the n term sequence.
#5- A for loop is used to iterate and calculate each term recursively.

def Fib(number): # function Fibonacci() is used to calculate the n term sequence.
    if(number == 1): # if(number == 1) check whether the given number is 1 or not.
        return 1
    elif(number == 2):
        return 2
    else:
        return (Fib(number - 2) + Fib(number - 1))
num = int(input("Enter the Range Number: "))
for n in range(1, num): # for loop is used to iterate and calculate each term recursively.
           print(Fib(n))