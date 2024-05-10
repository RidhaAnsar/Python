user = {
  'name' : 'milu',
  'age' : 23,
  'can_swim': True
}

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.items():
  key, value=item
  print(key, value)


for item in user.keys():
  print(item)

