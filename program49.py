#program to print the count words starting with a vowel

n="apple is orange umbrella cat"
c=n.split()
print(c)
d=0
for i in range(0,len(c)):
    if c[i].startswith(("a","e","i","o","u")):
        d+=1
print(d)
        
    

               