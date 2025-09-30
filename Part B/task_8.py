# Write a while loop that asks the user to enter a password until they type 'qa123'.

while True:
    password = input("Enter a password :")
    if password == "123":
        print("invalid password! please try again ")
    elif password == "asdjhakd":
        print("invalid password! please try again ")
    elif password == "":
        print("Enter any input")
    elif password == "qa123":
        print("Correct password")
        break
    else: 
        print("You are not entering correct password")

