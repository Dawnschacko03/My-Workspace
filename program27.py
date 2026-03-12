# program to count the number of uppercase and lowercase letters in a string
n="Hello World"
def count(n):
    c=0
    d=0
    for i in range(0,len(n),1):
        if n[i].isupper()==True:
            c+=1
        elif n[i].islower()==True:
            d+=1
    print("the number of uppercase letters are:",c)
    print("the number of lowercase letters are:",d)
count(n)
