# program to reverse a string
n="python"
def python(n):
    s=""
    for i in range(-1,-len(n)-1,-1):
        s+=n[i]
    print(s)
python(n)
