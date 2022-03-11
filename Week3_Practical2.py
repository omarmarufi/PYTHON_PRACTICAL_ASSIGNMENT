print("Enter Two Numbers: \n", end="")
no = int(input())
nt = int(input())

if no>nt:
    hcf = no
else:
    hcf = nt

while True:
    if no%hcf==0 and nt%hcf==0:
        break
    else:
        hcf = hcf - 1

print("\nHCF (" + str(no) + ", " + str(nt) + ") = ", hcf)