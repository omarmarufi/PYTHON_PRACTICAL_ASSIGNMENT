def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice( 1 - 2 - 3 - 4 ): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

#-------------------------------------------------------------------------------------

def Calc(n1, n2, op):
  ans = 0
  if op == '+':
    ans = n1 + n2
  elif op == '-':
    ans = n1 - n2
  elif op == '*':
    ans = n1 * n2
  elif op == '/':
    ans = n1 / n2
  else:
    ans = "Invalide Operator"
  return ans
num1, num2 = int(input("Enter the first number: ")), int(input("Enter the second number: "))
op = input("Enter the operator you want: ")
ans = Calc(num1, num2, op)
print("The answer: ", ans)

#----------------------------------------------------------------------------------------------------------------

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)
sum2 = float(num1) - float(num2)
sum3 = float(num1) * float(num2)
sum4 = float(num1) / float(num2)

choice = input('Enter an operator, + = addition, - = subtraction, * = multiplication and / = division: ')
if choice == '+':
  print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
  if choice == '-':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum2))
if choice == '*':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum3))
if choice == '/':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum4))