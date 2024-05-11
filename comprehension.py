some_list=['a', 'r', 'z', 'm', 'm', 'i', 'z', 'z']

duplicates=list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicates)
