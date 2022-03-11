from re import A

Number = int(input("Please Enter any Number: "))
total = 0
value = 1
while (value <= Number):
    total = total + value
    value = value + 1
Average = total / Number
print("The Sum of Natural Numbers from 1 to {0} :  {1}".format(Number , total))
print("Average of Natural Numbers from 1 to {0} :  {1}".format(Number , Average))

#----------------------------------------------------------------------------------- Second Method

Total = 0
a = 1

while a <= 10:
    Total += a
    a += 1
print(Total,"\n")
