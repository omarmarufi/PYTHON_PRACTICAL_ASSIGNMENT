Number = 1
while Number <= 10: #(Using while loop)
	print(Number)
	Number += 1


#------------------------------------------


Number = int(input("Enter a number: "))
print("The list of numbers from 1", "to", Number) 
for i in range(1, Number + 1): #(Using for loop)
    print ("\n", i , end = ' ')