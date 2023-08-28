stdata={'id':101,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata['sub'])
print(stdata.get('name'))"""

"""print(stdata)
print(stdata.keys())
print(stdata.values())

if 'python' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

#stdata["id"]=102
print(len(stdata))
stdata['city']='rajkot'
#stdata.pop('sub')
#del stdata['name']
stdata.clear()
print(stdata)



"""newdict=stdata.copy()
print(newdict)"""