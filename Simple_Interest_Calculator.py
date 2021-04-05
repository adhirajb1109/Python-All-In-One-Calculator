amount = float(input("Enter Amount : "))
rate = float(input("Enter Rate Of Interest : "))
time = float(input("Enter Time In Years : "))
simpleinterest = (amount * rate * time) / 100
print("Simple Interest = %0.3f"%(simpleinterest))