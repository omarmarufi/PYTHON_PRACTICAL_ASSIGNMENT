minimun_value = int(input("Enter minimun number: "))
maximun_value = int(input("Enter maximun number: "))

print("\nEven numbers from %d to %d are: " % (minimun_value, maximun_value))
for a in range(minimun_value , maximun_value + 1):
    if(a % 2 == 0):
        print(a , end = " - ")