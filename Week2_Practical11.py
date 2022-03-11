Number = int(input("Enter The Number: "))

if Number > 1:
    for i in range(2 , int(Number / 2) + 1):
        if (Number % i == 0):
            print(Number," is not a Prime Number")
            break
    else:
        print(Number," is a Prime number")
else:
    print(Number," is not a Prime number")