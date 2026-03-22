#program to print the second largest number
n=[1,34,5,23,67,33,55]
def count(n):
    n.sort()
    d=n[len(n)-2]
    print(d)
count(n)