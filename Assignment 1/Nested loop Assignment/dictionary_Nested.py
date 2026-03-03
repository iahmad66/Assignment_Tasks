# dic ={"tester1":20,"tester2":15,"tester3":18,'arr':[{"tester9":50},{"tester15":18}]}
# Find the maximum using nested loops 


def max_experience():
    dic ={"tester1":20,"tester2":15,"tester3":18,'arr':[{"tester9":50},{"tester15":18}]}
    max_experience = -1
    max_tester = " "
    for tester, experience in dic.items():
        if experience > max_experience:
                         max_experience = experience
                         max_tester = tester



max_experience()