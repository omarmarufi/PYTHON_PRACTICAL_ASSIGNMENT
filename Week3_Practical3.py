from ast import Num
from unicodedata import decimal

class Convert:
    def __init__(self , num):
        self.num = num
    def Binary(self):
        return bin(self.num)
    def Octal(self):
        return oct(self.num)
    def Hexadecimal(self):
        return hex(self.num)
if __name__ == '__main__':
    decimal = int(input("Enter the number: "))
    b = Convert(decimal)
    binary = b.Binary()
    print("Number in binary is =", binary)
    octal = b.Octal()
    print("Number in Octal is =", octal)
    hexadecimal = b.Hexadecimal()
    print("Number in hexadecimal is =", hexadecimal)

#-------------------------------------------------------------------------

decimal = int(input("Please Enter the decimal number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print(decimal, " Decimal = ", binary, "Binary Value")
print(decimal, " Decimal = ", octal, "Octal Value")
print(decimal, " Decimal = ", hexadecimal, "Hexadecimal Value")
