#program to find sum of series s=(1)+(1+2)+(1+2+3)+...+(1+2+3+...+n)
n=int(input(""))
def series(n):
    s=0
    s1=0
    for i in range(1,n+1):
        s+=i
        #s1=s+i
        #print(s)
        for j in range(1,n+1):
            s1=s+j
    print(s1)
series(n)