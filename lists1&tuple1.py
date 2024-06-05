l1=["hi", "hello", "morning", "goodday"]
l2=[1,2,3,4,5, ('a','b','c')]
print(l1, l2)
print(type(l1))
print(type(l2))
l3=list((2, 4,6))
print(l3)
tuple1=(1,2,3,4,5)
print(tuple1)
print(l3[0])
l1[0]="goodnight"
print(l1)
print(len(l1))
listcpy=l1.copy()  #copy method
print(listcpy)
l1.append(7)
a=[1,2,3,4,5,6]
b=a
print(b)