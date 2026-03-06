#Reverse of a number
r=1234789
def reverse(r):
    rev=0
    for i in range(len(str(r))-1,-1,-1):
        rev=rev*10+int(str(r)[i])
    print(rev)
reverse(r)