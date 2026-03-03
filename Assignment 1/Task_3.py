# 3. Write a program to count how many vowels are present in a given string. Example: 'automation' → 5 vowels.
string = str(input("Enter a string : "))
vowels = {"a", "e", "i", "o", "u"}
count = 0
for ch in string:   #to check all the ch
    if ch in vowels: #if ch available in vowels 
        count += 1
        
print("Vowels in string : ", count)