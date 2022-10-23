import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
def check():
    user_email = input("Enter your email :")
    if re.search(email_condition,user_email):
        print("Correct Email")
    else:
        print("Incorrect Email")



def repeat():
    while True:
        c = input("Do you want to check more mails? ")
        if c=='y':
            check()
            repeat()
        else:
            break

check()
repeat()