def find(number):
    number_type = "odd"
    if number%2 == 0:
        number_type="even"
    return number_type
number = int(input('Enter the number: '))
number_type = find(number)                         
print('Given number is',number_type)

#---------------------------------------------------------
def find(number):
    if number%2 == 0:
        return "even"
    return "odd"
number = int(input('Enter the number: '))
number_type = find(number)
print('Given number is',number_type)

#---------------------------------------------------------
def find(number):
    if number%2 == 0:
        numbertype="even"
    else:
        numbertype = "odd"
    return numbertype
number = int(input('Enter the number: '))
numbertype = find(number)
print('Given number is',numbertype)

