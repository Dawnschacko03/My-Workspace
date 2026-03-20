#program to print the odd and even numbers in the list and count
n=[1,2,3,4,4,5,6,77,79]
n1=[]
n2=[]
def sum(n):
    m=0
    l=0
    for i in range(0,len(n)):
        if n[i]%2==0:
            n1.append(n[i])
            m+=1
        else: 
            n2.append(n[i])
            l+=1
        print(n[i])

    print(n1)
    print(n2)
    print(m)
    print(l)
sum(n)
