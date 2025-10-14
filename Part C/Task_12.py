# 12. Write a program that reverses a string using a loop.

string = input("Enter any string value :")
reversed_str = " "

for ch in string:
    reversed_str = ch + reversed_str

print("reversed string is : " , reversed_str)
