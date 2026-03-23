#Program to rotate the list to the right
n=[1,2,3,4,5]
d=[]
d.insert(0,len(n))
for i in range(0,4):
    d.append(n[i])
print(d)


