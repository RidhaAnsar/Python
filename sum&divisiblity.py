sum=0
count=0
for i in range(100, 200):
  if(i%7==0):
    print(i)
    count=count+1
    sum=sum+i
print("SUM:",sum)
print("COUNT:",count)
