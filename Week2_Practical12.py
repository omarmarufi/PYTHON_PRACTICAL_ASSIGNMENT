Number = int(input("Enter a Number: "))
 
print("Prime numbers between", 1, "and", Number, "are: ")
for number in range(1, Number + 1):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)
     
#--------------------------------------------------------
num = int(input("Enter Any Number: "))
Number = 1
print("Prime numbers between", 1, "and", num, "are: ")
while(Number <= num):
    count = 0
    i = 2
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1