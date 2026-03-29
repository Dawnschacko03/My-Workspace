
#program to list the number zero on the rightmost
n=[1,0,2,1,1,0,2,0,0,3,4]
for i in range(0,len(n),1):
    if n[i]==0:
        n.remove(n[i])
        n.append(i)
    
print(n)