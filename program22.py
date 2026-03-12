# program to count the number of words in a string
n="hello my dear ku ku"
def rev(n):
    s=0
    x=n.split()
    print(x)
    for word in x:
        s+=1
    print(s)
rev(n)