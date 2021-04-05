costprice = float(input("Enter Cost Price : "))
sellingprice = float(input("Enter Selling Price : "))
quantity = float(input("Enter Quantity : "))
x = costprice - sellingprice
a = sellingprice - costprice
if x > 0 :
    loss = x *quantity
    print("Loss = %0.3f"%(loss))
    y = loss *100
    z = costprice * quantity
    losspercentage = y / z
    print("Loss Percentage = %0.3f"%(losspercentage) + " %")
else :
    profit = a * quantity
    print("Profit = %0.3f"%(profit))
    b = profit * 100
    c = costprice * quantity
    profitpercentage = b / c
    print("Profit Percentage = %0.3f"%(profitpercentage) + " %")
    

