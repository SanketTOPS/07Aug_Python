#class define
class studinfo:
    stid=12
    stname='Sanket'

    def getdata(self):
        print("This is getdata!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

#object of class
st=studinfo()
print(st.stid)
print(st.stname)
st.getdata()
st.getsum(23,45)