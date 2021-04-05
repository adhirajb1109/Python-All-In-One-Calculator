age = float(input("Enter Age : "))
if age > 1 and age < 61 :
    sal = float(input("Enter Annual Income : "))
    if sal < 250001:
        ttax = 0
        print("Income Tax = %0.3f"%(ttax))
    if sal > 250001 and sal < 500001:
        tax = 0.05 * (sal - 250000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
    if sal > 500001 and sal < 1000001:
        tax = 12500 + 0.2 * (sal - 500000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
    if sal > 1000001:
        tax = 112500 + 0.3 * (sal - 1000000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
if age > 60 and age < 80 :
    sal = float(input("Enter Annual Income : "))
    if sal < 300000 :
        ttax = 0
        print("Income Tax = %0.3f"%(ttax))
    if sal > 300000 and sal < 500000 :
        tax = 0.05 * (sal - 300000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f"%(ttax))
    if sal > 500000 and sal < 1000000 :
        tax = 10000 + 0.2 * (sal - 500000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
    if sal > 1000000 :
        tax = 110000 + 0.3 * (sal - 1000000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
if age > 80 :
    sal = float(input("Enter Annual Income : "))
    if sal < 500000 :
        ttax = 0
        print("Income Tax = %0.3f"%(ttax))
    if sal > 500000 and sal < 1000000 :
        tax = 0.2 *(sal - 500000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))
    if sal > 1000000 :
        tax = 100000 + 0.3 * (sal - 1000000)
        cess = 0.04 * tax
        ttax = tax + cess
        print("Income Tax = %0.3f" % (ttax))





