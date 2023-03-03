import re
email_conditon="^[a-z 0-9]+[._]*[a-z 0-9 ]+@[a-z 0-9]+\.[a-z]{2,}$"
email=input("enter your mail id:")

if re.search(email_conditon,email):
    print("valid email")
else:
    print("wrong email")