# 13. Write a program to print the multiplication table of 7 using range.


print("Multiplication table of 7 :")
sum = 0
num = 7
for i in range(1,11):
    i += sum
    print(str(num), " * " , i , "=" , i * num)
