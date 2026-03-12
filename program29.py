#program to remove vowels from a string
n="hello world"
def count(n):
    c=""
    for i in range(0,len(n),1):
        if n[i]!="a" and n[i]!="e" and n[i]!="i" and n[i]!="o" and n[i]!="u":
            c+=n[i]
    print(c)
count(n)