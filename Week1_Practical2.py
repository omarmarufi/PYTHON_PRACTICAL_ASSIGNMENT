p = float(input("Enter principal amount: "))
r = float(input("Enter Annual rate of interest: "))
t = float(input("Enter time in number of year: "))

si = p*r*t/100
ci = p* (1+r)**t

print("Simple interest is",si)
print("Compound interest is",ci)