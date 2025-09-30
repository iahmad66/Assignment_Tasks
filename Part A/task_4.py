# 4. Create a list of 5 student names. Convert it into a dictionary where the key is the student's index (starting from 1)
# and the value is the student's name.

Student_group = ["student1", "student2", "student3", "student4", "student5"]
student = dict(enumerate(Student_group, start= 1))
for index, value in student.items():
    print(index, value)