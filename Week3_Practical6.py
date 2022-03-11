import calendar

Year = int(input("Enter the year: "))
Month = int(input("Enter the month: "))

try:
    yourcalendar = calendar.month(Year , Month)
    print("\n", yourcalendar)
except IndexError:
    print("Its out of range")