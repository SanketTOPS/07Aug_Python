a=34

print("A:",a)

def getvalue():
    global a
    a=23
    print("A:",a)


getvalue()