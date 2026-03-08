#Sum of digits in a number
n=int(input(""))
def sum(n):
    sum1=0
    for i in range(len(str(n))-1,-1,-1):
        sum1+=int(str(n)[i])
    print(sum1)
sum(n)