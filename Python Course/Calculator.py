while True:
    print("Select Operator")
    print("1. Addition 2.Substraction 3.Multiplication 4.Division 5.Exit")

    choice = input("Please Enter Choice (1/2/3/4/5) :")
    
    if choice == '5':
        print("Exiting Calculator")
        break

    if choice in ('1', '2', '3', '4'):
        Number_1 = float(input("Please Enter First Number: "))
        Number_2 = float(input("Please Enter Second Number: "))

        if choice == '1':
            result = Number_1 + Number_2
        elif choice == '2':
            result = Number_1 - Number_2
        elif choice == '3':
            result = Number_1 * Number_2
        elif choice == '4' and Number_2 == 0:
            print("Error! Division by zero.")
        elif choice == '4':
            result = Number_1 / Number_2
        print("Result:", result)
    else:
        print("Invalid Input")
