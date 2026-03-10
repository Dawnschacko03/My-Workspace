#sum of series s=1+x+x^2+x^3+...+x^n
n=int(input(""))
x=int(input(""))
def series(x,n):
    s=0
    for i in range(0,n+1,1):
        #s=s+(x**i)
        s+=x**i
    print(s)
series(x,n)