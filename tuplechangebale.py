l1=["hi", "hello", "morning", "goodday"]

l2=list(l1)
l2[1]="hey"
l1=tuple(l2)
print(l1)