# Write a function to calculate the factorial of a number using a loop.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result
print("Factorial of number is : " , factorial(5))
