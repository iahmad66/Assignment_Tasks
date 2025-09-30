# Print the multiplication table of a number entered by the user (from 1 to 10).

num = int(input("Enter a number : "))
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
print("Enter number is :", num, "and the table of enter number is below")
for i in number:
    i + 1
    print(str(num), "x", str(i), "=", str(num * i))  # str(num) = convert int numbner into string
