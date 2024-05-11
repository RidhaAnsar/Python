#globalvar

total=1

def count():
  global total
  total+=1
  return total

print(count())
