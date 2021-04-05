n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
while n1%n2 != 0:
    rem = n1%n2
    n1=n2
    n2=rem
print("HCF = %0.3f"%(n2))
