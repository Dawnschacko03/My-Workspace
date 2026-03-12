# program to find the longest word in a string
n="my name is Dawnschacko"
def count(n):
    c=n.split()
    print(c)
    d=""
    e=0
    for word in c:
        if len(word)>e:
            e=len(word)
            d=word
    print(e)
    print(d)
count(n)
