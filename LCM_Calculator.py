n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))

for m in range (1, n1 *n2 +1):
    if m%n1 ==0 and m%n2 ==0 :
        print("LCM = %0.3f"%(m))
        break
