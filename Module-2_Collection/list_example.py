tech=['python','ios','java','ruby','php','JAVA']
"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3])
print(tech[:4])
print(tech[2:])
print(len(tech))

if 'JAVA' in tech:
    print("Yes...")
else:
    print("No..")"""

# ----------------------------------- #
"""print(tech)
tech[1]='Android'
print(tech)"""
# ----------------------------------- #

#print(tech)
"""for i in tech:
    print(i)"""

#print(tech.index('php'))

#python-0
#ios-1
#java-2

"""for i in tech:
    #print(i,tech.index(i))
    print(f"{i}-{tech.index(i)}")"""

# ------------ List Method -------------- #
"""print(tech)
tech.append('c++')
tech.insert(1,'html')"""
#tech.pop()
#tech.pop(1)
#tech.remove('php')
#del tech[0]
#tech.clear()
#del tech
#tech.reverse()
#tech.sort()
#print(tech)

# -------------------------------- #
print(tech)

"""newtech=['HTML','CSS','JS','Bootstrap']
print(newtech)
#print(tech+newtech)
#tech.extend(newtech)
#tech.append(newtech)
print(tech)"""


newtech=tech.copy()
print(newtech)