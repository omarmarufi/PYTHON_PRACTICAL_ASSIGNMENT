def lcm(a,b):
    lcm.multiple = lcm.multiple+b
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple=0
a = int(input("Enter first_number: "))
b = int(input("Enter second_number: "))
if(a>b):
    LCM = lcm(b,a)
else:
    LCM = lcm(a,b)
print(LCM)

#--------------------------------------------------------- Using While Loop

numOne = int(input("Enter the first_number: "))
numTwo = int(input("Enter the second_number: "))

if numOne > numTwo:
    lcm = numOne
else:
    lcm = numTwo
while True:
    if lcm % numOne == 0 and lcm % numTwo == 0:
        break
    else:
        lcm = lcm + 1
print("\nLCM =", lcm)

#-----------------------------------------------------------

print("Enter Two Numbers: ", end="")
try:
    nOne = int(input())
    try:
        nTwo = int(input())
        if nOne > nTwo:
            lcm = nOne
        else:
            lcm = nTwo
        while True:
            if lcm % nOne == 0 and lcm % nTwo == 0:
                break
            else:
                lcm = lcm + 1
        print("\nLCM (" + str(nOne) + ", " + str(nTwo)+") = ", lcm)
    except ValueError:
        print("\nInvalid Input!")
except ValueError:
    print("\nInvalid Input!")