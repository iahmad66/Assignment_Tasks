# Write a function that accepts a list of numbers and returns the largest number.


def find_largest(numbers):
    larger = numbers[0]
    for num in numbers:
        if num > larger:
            larger = num
    return larger


numbers = [1, 5, 10, 33, 4, 2, 5]
print("largest number in the list is : ", find_largest(numbers))
