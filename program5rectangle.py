l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
def rectangle(l,b):
    area=l*b
    print("area of the rectangle is:", area)
rectangle(l,b)

s=int(input("Enter the side of the square:"))
def square(s):
    area1=s*s
    per=4*s
    print("area and perimeter of the suare is:", area1, per, sep="\n")
square(s)