dictionary = {
  'greeting': 'hey',
'fruits':['apple', 'grapes'],
  'age':20
  
}
print(dictionary['greeting'])

print(dictionary.get('age'))

print('fruits' in dictionary)
print('size' in dictionary)
print(dictionary.items())


dict2=dictionary.copy()
print(dictionary)
print(dict2)


print(dictionary.update({'age':34}))
print(dictionary)
print(dictionary.pop('age'))
print(dictionary)
