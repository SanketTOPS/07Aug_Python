class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
class otherstudent(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)


st=studinfo()
st.getdata(1,'Sanket')

ot=otherstudent()
ot.getdata(2,'Mitesh')
