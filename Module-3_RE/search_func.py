import re

mystr="This is Python!"

x=re.search("this",mystr)
print(x)

if x: #true
    print("Match done!")
else:
    print("Error!Try again...")