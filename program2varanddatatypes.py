
x=5
y=4
z=x+y
z=z+1
x=y
y=z-x
print(x,y,z,sep="\t")


#Boolean data type
a=(5<6)
print(a)


#Complex data type
b=2+4j
print(b.real,b.imag,sep="\t")

#Floating Datatype
str1=20
str2=-3.1427
result1=float(str1)
print(result1)
result2=float(str2)
print(result2)

#String in python
string="Hello World"
print(string)

#List in python
list1=[1,2,3,4,5,6,7,3.145]
list2=[8,9,10,11,12,13,14,15]
print(list1+list2)
print(float(list1[7]+list2[6]))

#Tuple in python
tuple1=(1,2,3,4,5,6)
tuple2=(7,8,9,0,5.678)
print(tuple1+tuple2)
print(float(tuple1[5]+tuple2[2]))

#Dictionary in python
dict1={"name":"dawn","age":"23","gender":"male"}
print(dict1['name'],dict1['age'])
print(dict1['gender'])
print(dict1.keys())
print(dict1.values())