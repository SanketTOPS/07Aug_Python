stdata={}

#n=int(input("Enter number of pairs:"))
keys=['id','name','sub']

for i in range(len(keys)): #3
    v=input(f"Enter value of {keys[i]}:")
    stdata[keys[i]]=v

print(stdata)