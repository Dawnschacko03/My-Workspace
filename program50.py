#print the longest word number in a list
n=["end","elephant","baddie","thiruvananthapuram","dawn"]
d=0
c=[]
for i in range(0,len(n)):
    d=len(n[i])
    c.append(d)
print(c)
e=max(c)
print(e)
