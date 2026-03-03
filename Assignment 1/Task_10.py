# Given a list of numbers, print only the even numbers. Example: [10, 15, 22, 33, 40] → 10, 22, 40.

my_list = [2, 3, 4, 5, 6, 7, 8, 9]
for i in my_list:
    if (i % 2 == 0):  # i was using // instead of % it wont print anything then use chatgpt
        print(i, end=" ")  
