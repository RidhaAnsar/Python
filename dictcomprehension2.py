dict = {
  'a' : 1,
  'b' : 2
}
my_dict = {key:value**2 for key, value in dict.items() if value%2==0}
print(my_dict)
