# Form Validation

fnm=input("Enter your Firstname:")
lnm=input("Enter your Lastname:")


if fnm.isupper() and lnm.isupper(): #root
    print("Good...Now enter your email address!")
    email=input("Enter an Email:")
    if email.islower():
        print("Look's Good...Your data has been submitted!")
    else:
        print("Error! plz input proper email address")
else:
    print("Error!Plz input your firstname and lastname in capital only!")

