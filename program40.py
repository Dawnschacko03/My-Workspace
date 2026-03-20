#program to print the odd and even numbers in the list
n=[1,2,3,4,4,5,6,77,]
n1=[]
n2=[]
def count(n):
    for i in range(0,len(n)):
        if n[i]%2==0:
            n1.append(n[i])
            
        else: 
            n2.append(n[i])
        print(n[i])
    print(n1)
    print(n2)
count(n)
