fl=open('hello.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")

"""fl.write(stid)
fl.write(stnm)"""

fl.write(f"ID:{stid}\nName:{stnm}\n--------------\n")