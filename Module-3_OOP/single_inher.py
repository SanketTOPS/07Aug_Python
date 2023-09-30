class A:
    id=0
    name=''

    def getdata(self):
        self.id=input("Enter an ID:")
        self.name=input("Enter a Name:")

class B(A):
    def printdata(self):
        print("ID:",self.id)
        print("Name:",self.name)


objB=B()
objB.getdata()
objB.printdata()