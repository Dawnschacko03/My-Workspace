#program to list the number zero on the rightmost
n=[1,0,2,1,1,0,2,0,3,2,3,3,1]
for i in range(0,len(n),1):
        for j in range(0,len(n)-1,1):
            if n[j]==0:
                n[j],n[j+1]=n[j+1],n[j]
print(n)