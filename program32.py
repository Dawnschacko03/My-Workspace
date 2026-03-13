# program to count the number of occurrences of each character in a string
n="banana"
def count(n):
    c=""
    d=""
    checked=""
    for i in range(0,len(n),1):
        c=n[i]
        if c not in checked:
            checked+=c
            d=n.count(c)
            print(c,":",d)       
count(n)