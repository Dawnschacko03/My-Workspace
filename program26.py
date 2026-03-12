# program to extract only the alphabets from a string
n="abc123xyz"
def count(n):
    c=""
    for i in range(0,len(n),1):
        if n[i].isalpha()==True:
            c+=n[i]
        print(c)
count(n)