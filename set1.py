my_set={1,2,3,4,5}
my_set.add(100)
my_set.add(2)  #2 wont  be added again since it is already present:set 
                  #elements are unique
print(my_set)

my_list=[1,2,2,3,4,5,6,6,7]
print(set(my_list)) #will remove duplicate elements from the list

print( 3 in my_set)

print(len(my_set))
