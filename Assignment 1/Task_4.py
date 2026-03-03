#  Create a dictionary that stores the names of 3 testers and their years of experience.
#  Print the name of the tester with maximum experience.


def maximum_experience():
        QA_Team = {"Tester1": 1,"Tester2": 6 , "Tester3": 3}
        max_experience = -1
        max_tester = ""
        for tester, experience in QA_Team.items():
                if experience > max_experience:
                         max_experience = experience
                         max_tester = tester
                 
        print("Tester with Maximum experience is : ", max_experience)
maximum_experience()