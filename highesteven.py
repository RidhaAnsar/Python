def highest_even(n):
  evens=[]
  for item in n:
    if item%2==0:
      evens.append(item)
      return max(evens)

print (highest_even([12, 2, 3 , 5, 10]))
