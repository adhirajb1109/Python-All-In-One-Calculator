discount = float(input("Enter Discount Percentage: "))
markedprice = float(input("Enter Marked Price : "))
discountedprice = markedprice - ((discount/100)* markedprice)
print("You will have to pay ₹ %0.3f"%(discountedprice))
