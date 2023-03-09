print("1. Simple Interest")
print("2. Compound Interest")
choice = input("Enter your choice (1/2): ")
if choice == "1":
    principal = float(input("Enter the Principal Amount (in $): "))
    rate = float(input("Enter the Rate Of Interest per annum (in %): "))
    time = float(input("Enter the Time (in years): "))
    simple_interest = (principal * rate * time) / 100
    amount = principal + simple_interest
    print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {simple_interest}')
    print(f'Finally, the amount to be paid after {time} years is $ {amount}')
elif choice == "2":
    print("1. Compounded Annually")
    print("2. Compound Half-Yearly")
    print("3. Compounded Every 4 Months")
    print("4. Compounded Quarterly")
    print("5. Compounded Monthly")
    compounding_choice = input("Enter your choice (1/2/3/4/5): ")
    if compounding_choice == "1":
        principal = float(input("Enter the Principal Amount (in $): "))
        rate = float(input("Enter the Rate Of Interest per annum (in %): "))
        time = float(input("Enter the Time (in years): "))
        amount = round((principal * pow((1 + (rate / 100)), time)), 3)
        compound_interest = amount - principal
        print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {compound_interest}')
        print(f'Finally, the amount to be paid after {time} years is $ {amount}')
    elif compounding_choice == "2":
        principal = float(input("Enter the Principal Amount (in $): "))
        rate = float(input("Enter the Rate Of Interest per annum (in %): "))
        time = float(input("Enter the Time (in years): "))
        amount = round((principal * pow((1 + (rate / 200)), (2 * time))), 3)
        compound_interest = amount - principal
        print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {compound_interest}')
        print(f'Finally, the amount to be paid after {time} years is $ {amount}')
    elif compounding_choice == "3":
        principal = float(input("Enter the Principal Amount (in $): "))
        rate = float(input("Enter the Rate Of Interest per annum (in %): "))
        time = float(input("Enter the Time (in years): "))
        amount = round((principal * pow((1 + (rate / 300)), (3 * time))), 3)
        compound_interest = amount - principal
        print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {compound_interest}')
        print(f'Finally, the amount to be paid after {time} years is $ {amount}')
    elif compounding_choice == "4":
        principal = float(input("Enter the Principal Amount (in $): "))
        rate = float(input("Enter the Rate Of Interest per annum (in %): "))
        time = float(input("Enter the Time (in years): "))
        amount = round((principal * pow((1 + (rate / 400)), (4 * time))), 3)
        compound_interest = amount - principal
        print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {compound_interest}')
        print(f'Finally, the amount to be paid after {time} years is $ {amount}')
    elif compounding_choice == "5":
        principal = float(input("Enter the Principal Amount (in $): "))
        rate = float(input("Enter the Rate Of Interest per annum (in %): "))
        time = float(input("Enter the Time (in years): "))
        amount = round((principal * pow((1 + (rate / 1200)), (12 * time))), 3)
        compound_interest = amount - principal
        print(f'Interest to be paid on $ {principal} on the rate of {rate} % per annum after {time} years is $ {compound_interest}')
        print(f'Finally, the amount to be paid after {time} years is $ {amount}')
else:
    print("Error: Enter a valid choice !")
