# Ask the user to enter their age. If age < 18, print 'Minor'.
# If 18–60, print 'Adult'. If above 60, print 'Senior Citizen'.

age = int(input("please Enter your age : "))  # user must enter age number in int
if age < 18:
    print("Minor")
if 18 <= age <= 60:  # also age <= 60 and age >= 18:
    print("Adult")
if age > 60:
    print("Senior Citizen")
