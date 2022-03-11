def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))

n = 8
print("Fibonacci Sequence: \n")
for i in range(1 , n + 1):
    print(Fibonacci(i))