def sum(n):
  if n==0:
    return 0
  else:
    return n+sum(n-1)
result=sum(10)
print("sum of numbers from 0 to 10:",result)