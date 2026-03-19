# Program to find the largest element in a list
n=[1,2,3,4,5]
def count(n):
    for i in range(0,len(n),1):
        for j in range(1,len(n),1):
            if n[j]>n[i]: 
                m=n[j]
    print(m)
count(n)
