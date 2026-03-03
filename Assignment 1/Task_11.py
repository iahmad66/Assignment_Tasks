# Write a program to reverse a string using a loop. Example: 'Python' → 'nohtyP'.

string = "python"
for ch in reversed(string):  # repeat the string characters in reversed
    print(ch, end=" ")
