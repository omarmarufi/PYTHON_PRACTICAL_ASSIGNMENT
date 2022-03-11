a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2st number: "))
c = float(input("Enter the 3st number: "))
s = (a + b + c) / 2
area = (s*(s-a) * (s-b) * (s-c)) ** 0.5
print("The area is: %0.2f" %area)
