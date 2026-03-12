# program to check whether the string is palindrome or not
n=input("Enter the string:")
def palindrome(n):
    s=""
    for i in range(-1,-len(n)-1,-1):
        s+=n[i]
    print(s)
    if s==n:
        print("the string is palindrome")
    else:
        print("Not palindrome")
palindrome(n)