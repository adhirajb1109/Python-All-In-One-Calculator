print("Select Mode")
print("1.Convert Celsius To Fahrenheit")
print("2.Convert Fahrenheit To Celsius")
choice = input("Enter choice(1/2): ")
if choice =="1":
    c = float(input("Enter Temparature In Celsius :  "))
    a = c *1.8
    f = a + 32
    print("Temparature in Fahrenheit = %0.3f"%(f) + " °")
else :
    d = float(input("Enter Temparature In Fahrenheit :  "))
    b = d - 32
    e = b / 1.8
    print("Temparature in Celsius = %0.3f"%(e) + " °")
          
    

    



