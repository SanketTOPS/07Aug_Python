fl=open('new.txt','w')

for i in range(1,101):
    #print(i)
    fl.write(f"{str(i)}\n")