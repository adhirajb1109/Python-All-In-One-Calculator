print("Select Mode")
print("1.Perimeter")
print("2.Area/Surface Area")
print("3.Volume")
choicemode = input("Enter choice(1/2/3): ")
if choicemode == '1':
    print("Select Shape")
    print("1.Triangle")
    print("2.Square")
    print("3.Rectangle")
    print("4.Circle")
    choiceshape = input("Enter choice(1/2/3/4): ")
    if choiceshape == '1':
        sidetri1 = float(input('Enter Side A: '))
        basetriperi = float(input('Enter Base B: '))
        sidetri2 = float(input('Enter Side C: '))
        triperimeter = sidetri1 + basetriperi + sidetri2
        print('Perimeter Of Triangle =%0.3f' % (triperimeter))
    if choiceshape == '2':
        sidesqperi = float(input('Enter Side: '))
        sqperimeter = sidesqperi * 4
        print('Perimeter Of Square =%0.3f' % (sqperimeter))
    if choiceshape == '3':
        lengthperirec = float(input('Enter Length: '))
        breadthperirec = float(input('Enter Breadth: '))
        recperimeter = 2 * (lengthperirec + breadthperirec)
        print('Perimeter Of Rectangle =%0.3f' % (recperimeter))
    if choiceshape == '4':
        radiuspericir = float(input('Enter Radius: '))
        import math
        cirperimeter = 2 * math.pi * radiuspericir
        print('Perimeter / Circumference Circle =%0.3f' % (cirperimeter))
if choicemode == '2':
    print("Select Shape")
    print("1.Triangle")
    print("2.Square")
    print("3.Rectangle")
    print("4.Circle")
    print("5.Cube")
    print("6.Cuboid")
    print("7.Sphere")
    print("8.Lateral Surface Area (Cube)")
    print("9.Lateral Surface Area (Cuboid)")
    print("10.Right Angled Triangle (Pythagorean Theorem)")
    choiceshape1 = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
    if choiceshape1 == '1':
        baseareatri = float(input("Enter Base: "))
        heightareatri = float(input("Enter Height: "))
        areatri = baseareatri * heightareatri * 0.5
        print("Area Of Triangle = %0.3f" % (areatri))
    if choiceshape1 == '2':
        sqsidearea = float(input("Enter Side: "))
        areasq = sqsidearea * sqsidearea
        print("Area Of Square = %0.3f" % (areasq))
    if choiceshape1 == '3':
        lengtharearec = float(input("Enter Length: "))
        breadtharearec = float(input("Enter Breadth: "))
        arearec = lengtharearec * breadtharearec
        print("Area Of Rectangle = %0.3f" % (arearec))
    if choiceshape1 == '4':
        radiusareacir = float(input("Enter Radius: "))
        import math
        areacir = math.pi * (radiusareacir * radiusareacir)
        print("Area Of Circle = %0.3f" % (areacir))
    if choiceshape1 == '5':
        sidecuarea = float(input("Enter Side: "))
        areacu = 6 * (sidecuarea * sidecuarea)
        print("Surface Area Of Cube = %0.3f" % (areacu))
    if choiceshape1 == '6':
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))
        height = float(input("Enter Height: "))
        cuboidsurface = 2 * ((length * breadth) +
                             (breadth * height) + (height * length))
        print("Surface Area Of Cuboid = %0.3f" % (cuboidsurface))
    if choiceshape1 == '7':
        radiussphere = float(input("Enter Radius: "))
        import math
        surfaceareasphere = 4 * math.pi * (radiussphere * radiussphere)
        print("Surface Area Of Sphere = %0.3f" % (surfaceareasphere))
    if choiceshape1 == '8':
        laterallengthcube = float(input("Enter Length : "))
        lateralcube = 4 * (laterallengthcube ** 2)
        print("Lateral Surface Area Of Cube = %0.3f" % (lateralcube))
    if choiceshape1 == '9':
        laterallengthcuboid = float(input("Enter Length : "))
        lateralbreadthcuboid = float(input("Enter Breadth : "))
        lateralheightcuboid = float(input("Enter Height : "))
        lateralcuboid = 2 * lateralheightcuboid * \
            (laterallengthcuboid + lateralbreadthcuboid)
    if choiceshape1 == '10':
        print("1. Side A")
        print("2. Side B")
        print("3. Hypotenuse C")
        choice = input("Enter Choice (1/2/3) : ")
        if choice == "1":
            b = float(input("Enter Length Of Side B : "))
            hc = float(input("Enter Length Of Hypotenuse C : "))
            import math
            sidea = math.sqrt(((hc ** 2) - (b ** 2)))
            print("The Length Of Side A = %0.3f" % (sidea))
        if choice == "2":
            a = float(input("Enter Length Of Side A : "))
            hyc = float(input("Enter Length Of Hypotenuse C : "))
            import math
            sideb = math.sqrt(((hyc ** 2) - (a ** 2)))
            print("The Length Of Side B = %0.3f" % (sideb))
        if choice == "3":
            ah = float(input("Enter Length Of Side A : "))
            bh = float(input("Enter Length Of Side B : "))
            import math
            h = math.sqrt(((ah ** 2) + (bh ** 2)))
            print("Length Of Hypotenuse C = %0.3f" % (h))
if choicemode == '3':
    print("1.Cube")
    print("2.Cuboid")
    print("3.Sphere")
    choiceshape2 = input("Enter choice(1/2/3): ")
    if choiceshape2 == '1':
        sidevolume = float(input("Enter Side: "))
        cuvol = sidevolume ** 3
        print("Volume Of Cube = %0.3f" % (cuvol))
    if choiceshape2 == '2':
        lengthvol = float(input("Enter Length: "))
        breadthvol = float(input("Enter Breadth: "))
        heightvol = float(input("Enter Height: "))
        cuboidvol = lengthvol * breadthvol * heightvol
        print("Volume Of Cuboid = %0.3f" % (cuboidvol))
    if choiceshape2 == '3':
        rad = float(input("Enter Radius: "))
        import math
        volsph = 1.33333333333 * math.pi * (rad ** 3)
        print("Volume Of Sphere = %0.3f" % (volsph))
