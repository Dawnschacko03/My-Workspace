#program to remove occurences of an element
n=[1,2,1,1,2,3,2,3,3,2]
checked=[]
d=[]
for i in range(0,len(n)):
    if n[i] not in checked:
        d.append(n[i])
        checked.append(n[i])
print(d)

