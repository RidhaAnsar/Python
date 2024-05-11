my_list=[1,2,3]
def odd_num(item):
  return item%2!=0
  

print(list(filter(odd_num, my_list)))
print(my_list)
