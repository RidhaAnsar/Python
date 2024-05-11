#globalvar

a=5
b=10
c=a+b
def count():
  global a,b,c
  
  return c

print(count())
