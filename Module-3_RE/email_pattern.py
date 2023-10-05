import re

#sanket2020@gmail.com
email=input("Enter an email:")

email_pattern="[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,4}$"

x=re.findall(email_pattern,email)

if x: #true - match
    print("Valid email address!")
else:
    print("Error! Invalid Email")