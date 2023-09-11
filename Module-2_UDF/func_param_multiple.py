def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

n=int(input("Enter a number of students:")) #n=5

for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stsub=input("Enter Subject:")

    getdata(stid,stnm,stsub)





