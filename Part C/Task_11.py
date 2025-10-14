# 11. Create a dictionary of students and their scores. Loop through it and print only the names of students who scored above 50.

Dictionary = {"Student1":55, "Student2" : 40, "Student3" : 60 , "Student4" : 30 } 

for student in Dictionary:
    if Dictionary[student] > 50 :
        print("Students with score above then 50 : ", student)