# program to print pattern of a string
n=input("")
def pattern(n):
    for i in range(0,len(n)+1,1):
        print(n[:i])
pattern(n)