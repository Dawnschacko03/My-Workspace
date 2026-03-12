# program to count the number of vowels in a string
n="hello waooorld"
def count(n):
    c=0
    for i in range(0,len(n)-1,1):
        if n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u":
            c+=1
    print(c)
count(n)