# 16. Create a small text-based menu-driven program for a simple calculator with the following options:
#    1. Addition
#    2. Subtraction
#    3. Multiplication
#    4. Division
#    5. Exit

#    - The program should repeatedly ask the user to choose an option until they select Exit.
#    - Use functions for each operation.
#    - Example:
#      Enter first number: 10
#      Enter second number: 5
#      Choose operation: 1
#      Output: 15


def Add(num1, num2):
    sum = num1 + num2
    return sum


def Subtract(num1, num2):
    sub = num1 - num2
    return sub


def Multiply(num1, num2):
    multi = num1 * num2
    return multi


def Divide(num1, num2):
    Div = num1 / num2
    return Div


def menu():
    print("Choose option from (1,5)")
    while True:
        print("Menu Selection")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        Choose_option = input(" chose option from (1-5): ")

        if Choose_option in ["1", "2", "3", "4"]:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            if Choose_option == "1":
                print("Result :", Add(num1 , num2))
            elif Choose_option == "2":
                print("Result :", Subtract(num1 , num2))
            elif Choose_option == "3":
                print("Result :", Multiply(num1 , num2))
            elif Choose_option == "4":
                print("Result :", Divide(num1 , num2))
        else:
            print("Invalid option , please try again : ")

        if Choose_option == "5":
            print("Exit")
            break
            
        

menu()
