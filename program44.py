#program to count the freq of elements in the list
n=[1,2,1,1,3,2,3,3,1]
def sum(n):
    b=[]
    for i in range(0,len(n)):
        if n[i] not in b:
            a=n.count(n[i])
            b.append(n[i])
            print(n[i],a,sep=":")
sum(n)