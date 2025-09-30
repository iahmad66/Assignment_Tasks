# Write a program that accepts a username and password. If the username is 'admin' and the password is '1234', print 'Login Successful'.
# Otherwise, print 'Access Denied'.

user_name = input("Enter a user name : ")
password = input("Enter password :")

if user_name == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Access denied")
