#setcomprehension
my_list1={char for char in 'hello'}
my_list2={num for num in range(1,100)}
my_list3={num**2 for num in range(1,100)}
my_list4={num**2 for num in range(1,100) if num%2==0}
print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
