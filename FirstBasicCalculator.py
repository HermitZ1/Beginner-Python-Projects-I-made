 # The loop :o
while True:
# Printing the options for the user
        print("1 to Add")
        print("2 to Subtract")
        print("3 to Multiply")
        print("4 to Divide")
        print("Q to Exit")
    # Now time for input
        choice = input("Enter your choice : ")

        if choice == 'q' or choice == 'Q':
            break

        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
    # The if statements for whatever operation you want :P
        if choice == "1": 
            print(num1, "+", num2, "=", (num1+num2))
        elif choice == "2": 
            print(num1, "-", num2, "=", (num1-num2))
        elif choice == "3":
            print(num1, "*", num2, "=", (num1*num2))
        elif choice == "4":
            if num2 == 0.0:
                print("Error")
            else:
                print(num1, "/", num2, "=", (num1/num2))

        else:
            print("Pick something else god damn it")
