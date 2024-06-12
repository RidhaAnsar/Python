import json
x='{"name": "Ridha", "age": "21", "course":"MCA"}'

y=json.loads(x)
print(y)
print(y["age"])