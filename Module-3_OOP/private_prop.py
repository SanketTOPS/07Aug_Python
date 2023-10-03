class studinfo:
    __stid=12 #private
    __stnm='Sanket' #private

    def __getdata(self): 
        print("This is getdata!")

        print("ID:",self.__stid)
        print("Name:",self.__stnm)

    def printdata(Self):
        Self.__getdata()

st=studinfo()
#st.getdata()
"""print(st.__stid)
print(st.__stnm)"""

st.printdata()