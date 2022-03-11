def leap(year):
    if(year % 400 == 0):
        print(year,"Is a leap year")
    elif(year % 400 == 0 and year % 100 != 0):
        print(year,"Is leap year")

    else:
        print(year,"Is not a leap year")

year = int(input("Enter the year: "))
leap(year)