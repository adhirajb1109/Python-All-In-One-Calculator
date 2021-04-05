a = float(input("Enter Height (In Metres): "))
b = float(input("Enter Weight (In Kilograms): "))
c = b / (a ** 2)
print("BMI = %0.3f"%(c))
if c < 18 :
    print("You Are Underweight")
if c > 18 and c < 25 :
    print("You Are Healthy")
if c > 25 and c < 30 :
    print("You Are Overweight")
if c > 30 :
    print("You Are Obese")

