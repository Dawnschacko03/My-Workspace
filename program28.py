# program to count the number of consonants in a string
n="hello world"
def count(n):
    c=0
    for i in range(0,len(n)-1,1):
        if n[i]!="a" and n[i]!="e" and n[i]!="i" and n[i]!="o" and n[i]!="u":
            c+=1
    print(c)
count(n)