# program to check if two strings are anagrams or not
n="aab"
m="abb"
def count(n,m):
    if len(n)==len(m):
        c=""
        checked=""
        for i in range(0,len(n),1):
            c=n[i]
            if c in m and c not in checked:
                checked+=c
        if checked==n:
            print("Anagram")
        else:
            print("Not Anagram")
           
count(n,m)