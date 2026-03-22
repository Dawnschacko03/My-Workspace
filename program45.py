#prorgram to find common elements between two lists
n=[1,2,3,4,5]
m=[4,5,6,7,8]
def sum(n,m):
    a=0
    b=[]
    for i in range(0,len(n)):
        if n[i] in m:
            a=n[i]
            b.append(a)
    print(b)
sum(n,m)