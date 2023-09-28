class studinfo:
    stid=1
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Calling via Object
"""st=studinfo()
st.getdata()
st.stid=2
st.stnm='Ashok'
st.getdata()"""

#Calling via Instance
studinfo().getdata()
studinfo().stid=2
studinfo().stnm='Nirav'
studinfo().getdata()