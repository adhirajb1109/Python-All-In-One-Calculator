cost = float(input("Enter Cost Of Product / Service : "))
gstper = float(input("Enter GST Percentage : "))
gst = cost * gstper/100
amount = cost + gst
print("GST = ₹ %0.3f"%(gst))
print("Net Price = ₹ %0.3f"%(amount))
