from fractions import Fraction
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Of")
choice = input("Enter Choice (1/2/3/4/5) : ")
if choice == "1":
    cv = input("Enter A Fraction : ")
    dv = Fraction(cv)
    ev = input("Enter Second Fraction : ")
    fv = Fraction(ev)
    gv = dv + fv
    print("Sum is equal to %0.3f" % (gv))
if choice == "2":
    cv = input("Enter A Fraction : ")
    dv = Fraction(cv)
    ev = input("Enter Second Fraction : ")
    fv = Fraction(ev)
    gv = dv - fv
    print("Difference is equal to %0.3f" % (gv))
if choice == "3":
    la = input("Enter A Fraction : ")
    ls = Fraction(la)
    lk = input("Enter Second Fraction : ")
    pl = Fraction(lk)
    li = ls * pl
    print("Product is equal to %0.3f" % (li))
if choice == "4":
    oi = input("Enter A Fraction : ")
    di = Fraction(oi)
    pn = input("Enter Second Fraction : ")
    op = Fraction(pn)
    lcv = di / op
    print("Quotient is equal to %0.3f" % (lcv))
if choice == "5":
    lol = input("Enter A Fraction : ")
    dol = Fraction(lol)
    pol = input("Enter Second Fraction : ")
    rol = Fraction(pol)
    mam = dol * rol
    print("Answer is equal to %0.3f" % (mam))