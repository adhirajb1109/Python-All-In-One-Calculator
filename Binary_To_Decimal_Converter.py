print("1. Decimal To Binary")
print("2. Binary To Decimal")
choice = input("Enter Choice (1/2) : ")
if choice == "1":
    def decimalToBinary(num):

        if num > 1:
            decimalToBinary(num // 2)
        print(num % 2, end='')

    number = int(input("Enter Decimal Number: "))
    decimalToBinary(number)
if choice == "2":
    binary_string = input("Enter Binary Number :")
    try:
        decimal = int(binary_string, 2)
        print("The decimal value is :", decimal)
    except ValueError:
        print("Invalid binary number")
