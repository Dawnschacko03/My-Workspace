
n=[1,2,4,5,6,7]
def missing(n):
    c=1
    for i in range(0,len(n)):
        #for j in range(0,n[-1]):
        if c==n[i]:
            c+=1
            print(n[i])
        #print(n[i],c)#n[j])d)
missing(n)